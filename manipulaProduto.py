import manipulaCSV as mcsv
import apresentacao


def carregar() -> list:
    '''
    Carrega a lista de produtos do arquivo produto.csv
    
    Retorno
    -------
    Retorna uma lista de dicionários com os produtos lidos
    '''
    listaProdutos = mcsv.carregarDados("Produtos.csv")
    return listaProdutos

def cadastrar(listaProdutos: list ) -> bool :
    apresentacao.limpaTela()
    prod = apresentacao.CadastrarProduto()
    listaProdutos.append(prod) 
    campos = ["Id","Setor","Nome","Preco","Validade","Quantidade"] 
    return mcsv.gravarDados("Produtos.csv",campos, listaProdutos)

def editar() -> bool:
    apresentacao.limpaTela()
    id = apresentacao.EditarProduto()
    produtos = carregar()
    for i in range(len(produtos)):
        if produtos[i]["Id"] == id:
            produtos[i] = apresentacao.CadastrarProduto()
            campos = ["Id","Setor","Nome","Preco","Validade","Quantidade"]
            return mcsv.gravarDados("Produtos.csv",campos, produtos)
    return False
