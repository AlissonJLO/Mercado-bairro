import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaProduto as mprod
import apresentacao
import time
import csv
from datetime import datetime
import os

def carregar() -> list:
    '''
    Carrega a lista de vendas do arquivo vendas.csv

    Retorno
    -------
    Retorna uma lista de dicionários com as vendas lidas
    '''
    listaVendas = mcsv.carregarDados("Data/Vendas.csv")
    return listaVendas


def nova_Venda() -> bool:
    '''
    Cadastra uma nova venda

    Retorno
    -------
    Retorna True se a venda foi cadastrada com sucesso, False caso contrário
    '''
    apresentacao.limpaTela()
    venda = apresentacao.efetuar_venda()
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
        vendas_cliente = (vendas, cpf)
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
def obter_ultima_identificacao_venda():
    if os.path.exists("Vendas.csv") and os.path.getsize("Vendas.csv") > 0:
        with open("Vendas.csv", "r") as vendas_file:
            vendas_reader = csv.reader(vendas_file)
            last_row = None
            for row in vendas_reader:
                last_row = row
            return int(last_row[0]) if last_row else 0
    else:
        return 0



def registrar_venda(cpf: str, lista_compras: list):
    # Obter a última identificação de venda e incrementar 1 para a nova identificação
    ultima_identificacao_venda = obter_ultima_identificacao_venda()
    nova_identificacao_venda = ultima_identificacao_venda + 1
    data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Calcular o valor total da venda
    valor_total = sum(item['Preco'] * item['Quantidade'] for item in lista_compras)
    quantidade_total = sum(item['Quantidade'] for item in lista_compras)

    # Registrar a venda em "Vendas.csv"
    with open("Data/Vendas.csv", "a", newline='') as vendas_file:
        vendas_writer = csv.writer(vendas_file)
        vendas_writer.writerow([nova_identificacao_venda, cpf, data_venda, valor_total, quantidade_total])

    # Adicionar itens comprados em "ItensCompra.csv"
    with open("Data/ItensCompra.csv", "a", newline='') as itens_compra_file:
        itens_compra_writer = csv.writer(itens_compra_file)
        for item in lista_compras:
            id_produto = item['Id']
            quantidade = item['Quantidade']
            preco_unitario = item['Preco']
            preco_total = quantidade * preco_unitario
            itens_compra_writer.writerow([nova_identificacao_venda, cpf, id_produto, quantidade, preco_unitario, preco_total])


def atualizar_estoque(id_produto: str, quantidade_vendida: int):
    # Ler o arquivo de produtos e atualizar o estoque
    with open("Data/Produtos.csv", "r") as produtos_file:    
        produtos_reader = csv.DictReader(produtos_file)
        produtos = list(produtos_reader)
        print
    for produto in produtos:
        if produto['Id'] == id_produto:
            print("Nome do Produto:", produto['Nome'])
            print("Preço do Produto:", produto['Preco'])
            print("Quantidade em Estoque:", produto['Quantidade'])
            return
    print(f"Produto com ID: {id_produto} não encontrado.")
