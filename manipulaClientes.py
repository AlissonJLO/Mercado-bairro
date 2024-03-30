import manipulaCSV as mcsv
import apresentacao


def carregar() -> list:
    '''
    Carrega o arquivo de Cliente.csv numa lista

    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("Data/Cliente.csv")
    return lista


def carregarVendas() -> list:
    '''
    Carrega o arquivo de Cliente.csv numa lista

    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    listavenda = mcsv.carregarDados("Data/Vendas.csv")
    return listavenda






def cadastrarCli() -> bool:
    apresentacao.limpaTela()
    listaClientes = carregar()
    cliente = apresentacao.CadastrarClientes()
    listaClientes.append(cliente)
    camposCliente = ['nome', 'cpf', 'cidade', 'estado', 'endereco', 'idade', 'data_nascimento', 'pontos']

    return mcsv.gravarDados('Data/Cliente.csv', camposCliente, listaClientes)


def editarCli() -> bool:
    apresentacao.limpaTela()
    cpf = apresentacao.EditarClientes()
    clientes = carregar()
    cliente_encontrado = False
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            cliente_encontrado = True
            cliente_atualizado = apresentacao.CadastrarClientes()
            cliente.update(cliente_atualizado)
            camposCliente = ['nome', 'cpf', 'cidade', 'estado', 'endereco', 'idade', 'data_nascimento', 'pontos']
            sucesso = mcsv.gravarDados('Data/Cliente.csv', camposCliente, clientes)

            print("Dados gravados com sucesso." if sucesso else "Falha ao gravar dados.")
            return sucesso

    if not cliente_encontrado:
        print(f"Cliente com o cpf : {cpf} fornecido não encontrado.")

    return False





def excluir(listaClientes: list, cpf: str) -> bool:
    '''
    Excluir um cliente da lista de clientes e atualiza o arquivo CSV
    '''
    flag = False
    camposCliente = list(listaClientes[0].keys())
    for i, cliente in enumerate(listaClientes):
        if cliente['CPF'] == cpf:
            flag = True
            listaClientes.pop(i)
    # print(listaClientes)
    if flag:
        mcsv.gravarDados("Data/Cliente.csv", camposCliente, listaClientes)
    return flag


def atualizarPontos():
    return True


def atualizarCliente():
    return True


def atualizarPontos():
    # Carregar os clientes e as vendas dos arquivos CSV
    # clientes = mcsv.carregarDados("Data/Cliente.csv")
    # vendas = mcsv.carregarDados("Data/Vendas.csv")

    clientes = carregar()
    vendas = carregarVendas()

    pontos_por_cpf = {}

    for venda in vendas:
        cpf = venda['CPF']
        total = float(venda['Total'])  
        pontos_por_cpf[cpf] = pontos_por_cpf.get(cpf, 0) + total

    for cliente in clientes:
        cpf = cliente['cpf']
        if cpf in pontos_por_cpf:
            cliente['pontos'] = pontos_por_cpf[cpf]
    camposCliente = ['nome', 'cpf', 'cidade', 'estado', 'endereco', 'idade', 'data_nascimento', 'pontos']
    sucesso = mcsv.gravarDados('Data/Cliente.csv', camposCliente, clientes)
    return sucesso