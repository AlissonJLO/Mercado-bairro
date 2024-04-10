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
    campos = ['Id-Venda','CPF','Data,Total','Quantidade-Produtos']
    return mcsv.gravarDados("Data/Vendas.csv", campos, vendas)



