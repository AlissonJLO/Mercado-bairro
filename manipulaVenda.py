import manipulaCSV as mcsv
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


def novaVenda() -> bool:
    '''
    Cadastra uma nova venda

    Retorno
    -------
    Retorna True se a venda foi cadastrada com sucesso, False caso contrário
    '''
    apresentacao.limpaTela()
    venda = apresentacao.CadastrarVenda()
    vendas = carregar()
    vendas.append(venda)
    campos = ["Id", "Cliente", "Data", "Produtos", "Valor"]
    return mcsv.gravarDados("Data/Vendas.csv", campos, vendas)


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
