import manipulaCSV as mcsv
import manipulaProduto as mprod
import apresentacao

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

def BaixaEstoque(idProduto, quantidade):
    produtos = mprod.carregar()
    for produto in produtos:
        if idProduto == produto['Id-Produto']:
            quantidadeAtual = int(produto['Quantidade'])
            novaQuantidade = quantidadeAtual - int(quantidade)
            produto['Quantidade'] = str(novaQuantidade)

    mcsv.gravarDados("Data/Produtos.csv", ['Id-Produto', 'Setor',
                      'Nome', 'Preco', 'Validade', 'Quantidade'], produtos)

def listarVendas():
    apresentacao.limpaTela()
    apresentacao.listar_vendas()
    
