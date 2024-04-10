import manipulaCSV as mcsv
import manipulaVenda as mvend
import manipulaItensCompra as mitc
from datetime import datetime, timedelta
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
    apresentacao.limpaTela()
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


def produtoSetor():
    apresentacao.limpaTela()
    setor = input("Informe o setor do produto: ")
    setoresValidos = ["Higiene", "Limpeza",
                      "Bebidas", "Frios", "Padaria", "Açougue"]
    while setor not in setoresValidos:
        print("Setor inválido. Setores válidos: Higiene, Limpeza, Bebidas, Frios, Padaria, Açougue")
        produto['Setor'] = input("Setor do produto: ")
    produtos = carregar()
    produtos_setor = [
        produto for produto in produtos if produto["Setor"] == setor]

    if len(produtos_setor) > 0:
        print(f"Produtos do setor {setor}:")
        for produto in produtos_setor:
            print(f"ID: {produto['Id']}, Nome: {produto['Nome']}, Preço: R${produto['Preco']}, Validade: {produto['Validade']}, Quantidade em estoque: {produto['Quantidade']}")
    else:
        print(f"Não há produtos no setor {setor}.")

    input("Pressione ENTER para voltar...")


def maisVendidos():
    vendas = mvend.carregar()
    itensCompra = mitc.carregar()
    produtos = carregar()

    # Obter a data de 3 dias atrás
    tres_dias_atras = datetime.now() - timedelta(days=3)

    # Filtrar vendas dos últimos 3 dias
    vendas_recentes = [venda for venda in vendas if datetime.strptime(
        venda['Data'], "%d/%m/%Y") >= tres_dias_atras]

    # Mapear ID do produto para o nome do produto
    nome_por_id = {produto['Id']: produto['Nome'] for produto in produtos}

    # Contabilizar a quantidade vendida de cada produto pelo nome
    quantidade_por_produto = {}
    for item in itensCompra:
        if any(venda['Id-Venda'] == item['Id-Venda'] for venda in vendas_recentes):
            nome_produto = nome_por_id[item['Id-Produto']]
            if nome_produto in quantidade_por_produto:
                quantidade_por_produto[nome_produto] += int(item['Quantidade'])
            else:
                quantidade_por_produto[nome_produto] = int(item['Quantidade'])

    # Ordenar os produtos pela quantidade vendida
    mais_vendidos = sorted(quantidade_por_produto.items(),
                           key=lambda x: x[1], reverse=True)

    # Exibir os cinco produtos mais vendidos
    apresentacao.limpaTela()
    print("Os 5 produtos mais vendidos nos últimos 3 dias são:")
    if len(mais_vendidos) == 0:
        apresentacao.limpaTela()
        print("Nenhum produto vendido nos últimos 3 dias.")
    else:
        for nome, quantidade in mais_vendidos[:5]:
            print(f"Produto: {nome} - Quantidade: {quantidade}")
    input("Pressione ENTER para voltar...")

    return True


''''
mitc.carregar() retorna uma lista de dicionários com os itens de compra
mvend.carregar() retorna uma lista de dicionários com as vendas
'''
