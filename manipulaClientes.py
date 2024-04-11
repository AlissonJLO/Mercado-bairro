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


def novaVenda() -> bool:
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
    #salva vednda no arquivo vendas.csv
    campos = ['Id-Venda','CPF','Data', 'Total', 'Quantidade-Produtos']
    return mcsv.gravarDados("Data/Vendas.csv", campos, vendas)


def gerar_id_venda():
    '''
    busca id venda em "Vendas.csv"
    ------
    retorna gera um id baseado na ultima venda +1
    '''
    vendas = carregar()
    if not vendas:
        return 1  # Se não houver vendas, o próximo ID será 1
    
    ultimo_dict = vendas[-1]
    ultimo_id = ultimo_dict.get("Id-Venda", 0)  # Obtém o último ID de venda, se não existir, assume 0
    return ultimo_id + 1  # Incrementa o último ID de venda em 1


def vendas_do_cliente():
    apresentacao.limpaTela()
    # verifica se o CPF é cadastrado
    cpf = apresentacao.ler_cpf()
    clientes = mcli.carregar()            
    cadastro = mcli.checar_cadastro(clientes, cpf)
    if cadastro:            
        #cadastro encontrado
        vendas = carregar()
        vendas_cliente = listar_vendas(vendas,cpf)
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
