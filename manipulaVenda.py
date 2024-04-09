import manipulaCSV as mcsv
import manipulaClientes as mcli
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
    venda = apresentacao.Criar_Nova_Venda()
    vendas = carregar()
    vendas.append(venda)
    campos = ["Id", "Cliente", "Data", "Produtos", "Valor"]
    return mcsv.gravarDados("Data/Vendas.csv", campos, vendas)

def vendas_do_cliente():
    apresentacao.limpaTela()
    # verifica se o CPF é cadastrado
    cpf = apresentacao.ler_cpf()
    clientes = mcli.carregar()            
    cadastro = mcli.checar_cadastro(clientes, cpf)
    if cadastro:            
        #cadastro encontrado
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



def exibir_info_produto(id_produto):
    '''
    exibe informações do produto conforme o Id digitado
    '''
    produtos = mprod.carregar()
    for produto in produtos:
        if produto['Id'] == id_produto:
            print("Nome do Produto:", produto['Nome'])
            print("Preço do Produto:", produto['Preco'])
            print("Quantidade em Estoque:", produto['Quantidade'])
            return
    print(f"Produto com ID: {id_produto} não encontrado.")
