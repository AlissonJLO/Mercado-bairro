import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaProduto as mprod
import apresentacao
import time


def carregar() -> list:
    '''
    Carrega a lista de vendas do arquivo vendas.csv

    Retorno
    -------
    Retorna uma lista de dicionários com as vendas lidas
    '''
    listaVendas = mcsv.carregarDados("Data/Vendas.csv")
    return listaVendas


def novaVenda() -> bool:
    '''
    Cadastra uma nova venda

    Retorno
    -------
    Retorna True se a venda foi cadastrada com sucesso, False caso contrário
    '''
    apresentacao.limpaTela()
    vendas = apresentacao.efetuar_venda()
    campos = ['Id-Venda', 'CPF', 'Data', "Total", 'Quantidade-Produtos']
    return mcsv.gravarDados("Data/Vendas.csv", campos, vendas)


def vendas_do_cliente():
    apresentacao.limpaTela()
    # verifica se o CPF é cadastrado
    cpf = apresentacao.ler_cpf()
    clientes = mcli.carregar()
    cadastro = mcli.checar_cadastro(clientes, cpf)
    if cadastro:
        # cadastro encontrado
        vendas = carregar()
        vendas_cliente = listar_Vendas_Clientes(vendas, cpf)
        print(vendas_cliente)
        input("enter para voltar\n")
    else:
        # CPF não encontrado, redirecionar para cadastro
        print("CPF fornecido não cadastrado.\nRedirecionando para cadastro...\n")
        time.sleep(3)
        mcli.cadastrarCli()


def listar_Vendas_Clientes(vendas, cpf) -> list:
    '''
    Lista as vendas de um determinado cliente

    Retorno
    -------
    Retorna uma lista de dicionários com as vendas do cliente informado
    '''
    vendas_cliente = []
    for linha in vendas:
        if "CPF" in linha and linha["CPF"] == cpf:
            vendas_cliente.append(dict(linha))

    return vendas_cliente


def precoProduto(idProduto):
    '''
    Retorno
    -------
    Retorna o preço do produto
    '''
    produtos = mprod.carregar()
    for produto in produtos:
        if produto['Id-Produto'] == idProduto:
            return produto['Preco']
    return 0
