import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaProduto as mprod
import apresentacao
import time
from datetime import datetime


def carregar() -> list:
    '''
    Carrega a lista de vendas do arquivo vendas.csv

    Retorno
    -------
    Retorna uma lista de dicionários com as vendas lidas
    '''
    listaVendas = mcsv.carregarDados("Data/Vendas.csv")
    return listaVendas

# Id-Venda;CPF;Id-Produto;Quantidade;Preço-Unitario;Preco-Total itensCompra.csv
# Id-Venda;CPF;Data;Total;Quantidade-Produtos Vendas.csv


def novaVenda():
    apresentacao.limpaTela()
    itens_venda = apresentacao.efetuar_venda()

    camposVendas = ['Id-Venda', 'CPF', 'Data', 'Total', 'Quantidade-Produtos']
    camposItens = ['Id-Venda', 'CPF', 'Id-Produto',
                   'Quantidade', 'Preco-Unitario', 'Preco-Total']

    sucessoVendas = mcsv.gravarDados(
        "Data/Vendas.csv", camposVendas, itens_venda['vendas'])
    if not sucessoVendas:
        print("Falha ao gravar dados de vendas.")

    sucessoItens = mcsv.gravarDados(
        "Data/ItensCompra.csv", camposItens, itens_venda['itensCompra'])
    if not sucessoItens:
        print("Falha ao gravar itens da compra.")

    print("Venda cadastrada com sucesso.")


def vendas_do_cliente():
    apresentacao.limpaTela()
    # verifica se o CPF é cadastrado
    cpf = apresentacao.ler_cpf()
    clientes = mcli.carregar()
    cadastro = mcli.checar_cadastro(clientes, cpf)
    if cadastro:
        # cadastro encontrado
        vendas = carregar()
        vendas_cliente = listar_vendas(vendas, cpf)
        print(vendas_cliente)
        input("enter para voltar\n")
    else:
        # CPF não encontrado, redirecionar para cadastro
        print("CPF fornecido não cadastrado.\nRedirecionando para cadastro...\n")
        time.sleep(3)
        mcli.cadastrarCli()


def listar_vendas(vendas, cpf):
    vendas_cliente = []
    for venda in vendas:
        if venda["CPF"] == cpf:
            vendas_cliente.append(venda)
    return vendas_cliente


def BaixaEstoque(idProduto, quantidade):
    produtos = mprod.carregar()
    for produto in produtos:
        if idProduto == produto['Id-Produto']:
            quantidadeAtual = int(produto['Quantidade'])
            novaQuantidade = quantidadeAtual - int(quantidade)
            produto['Quantidade'] = str(novaQuantidade)

    mcsv.gravarDados("Data/Produtos.csv", ['Id-Produto', 'Setor',
                      'Nome', 'Preco', 'Validade', 'Quantidade'], produtos)
# Id-Produto;Setor;Nome;Preco;Validade;Quantidade
