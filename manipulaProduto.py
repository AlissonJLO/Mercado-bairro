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


def cadastrar() -> bool:
    apresentacao.limpaTela()
    listaProdutos = carregar()
    prod = apresentacao.CadastrarProduto()
    listaProdutos.append(prod)
    campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
    return mcsv.gravarDados("Data/Produtos.csv", campos, listaProdutos)


def editar() -> bool:
    apresentacao.limpaTela()
    id = apresentacao.EditarProduto()
    produtos = carregar()
    produto_encontrado = False
    for produto in produtos:
        if produto["Id"] == id:
            produto_encontrado = True
            produto_atualizado = apresentacao.CadastrarProduto()
            produto.update(produto_atualizado)
            campos = ["Id", "Setor", "Nome", "Preco", "Validade", "Quantidade"]
            sucesso = mcsv.gravarDados("Data/Produtos.csv", campos, produtos)
            print("Dados gravados com sucesso." if sucesso else "Falha ao gravar dados.")
            return sucesso

    if not produto_encontrado:
        print("Produto com o ID fornecido não encontrado.")

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
