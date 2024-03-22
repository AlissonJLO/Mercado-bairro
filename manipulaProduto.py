import manipulaCSV as mcsv
import apresentacao


def carregar() -> list:
    '''
    Carrega a lista de produtos do arquivo produto.csv

    Retorno
    -------
    Retorna uma lista de dicionários com os produtos lidos
    '''
    listaProdutos = mcsv.carregarDados("Data/Produtos.csv")
    return listaProdutos


def cadastrar(listaProdutos: list) -> bool:
    apresentacao.limpaTela()
    prod = apresentacao.CadastrarProduto()
    listaProdutos.append(prod)
    campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
    return mcsv.gravarDados("Data/Produtos.csv", campos, listaProdutos)


def editar() -> bool:
    apresentacao.limpaTela()
    id = apresentacao.EditarProduto()
    produtos = carregar()
    for i in range(len(produtos)):
        if produtos[i]["Id"] == id:
            produtos[i] = apresentacao.CadastrarProduto()
            campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
            return mcsv.gravarDados("Data/Produtos.csv", campos, produtos)
    return False

def estoqueSetor(setor: str) -> list:
    '''
    Retorna uma lista de produtos de um determinado setor

    Parâmetros
    ----------
    setor : str
        Setor dos produtos a serem listados

    Retorno
    -------
    Retorna uma lista de dicionários com os produtos do setor informado
    '''
    produtos = carregar()
    return [p for p in produtos if p["Setor"] == setor]

def estoqueBaixo() -> list:
    '''
    Retorna uma lista de produtos com estoque baixo

    Retorno
    -------
    Retorna uma lista de dicionários com os produtos com estoque baixo
    '''
    produtos = carregar()
    return [p for p in produtos if p["Quantidade"] < 10]

def maisVendido() -> dict:
    '''
    Retorna o produto mais vendido

    Retorno
    -------
    Retorna um dicionário com o produto mais vendido
    '''
    produtos = carregar()
    maisVendido = produtos[0]
    for p in produtos:
        if p["Quantidade"] < maisVendido["Quantidade"]:
            maisVendido = p
    return maisVendido
