from os import system, name
import manipulaClientes as mcli
import manipulaProduto as mprod
import manipulaVenda as mvend

#################################################################


def limpaTela():
    '''
    Limpa a tela de acordo com o systema operacional (Windows ou Linux)
    '''
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

#################################################################


def MenuPrincipal() -> str:
    '''
    Exemplo de Menu principal para o sistema

    Retorno    
    -------
    Retorna válida escolhida

    '''
    opcoes = [1, 2, 3, 9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print("1.Venda\n2.Clientes\n3.Produto\n9.Sair")
        print('#'*20)
        opcao = int(input("Opção -> "))
    return opcao

#################################################################


def MenuProduto():
    while True:
        limpaTela()
        print("#"*20)
        print(
            "1.Cadastrar novo produto\n2.Atualizar imformaçoes do produto\n3.Busca produtos por setor\n4.Produtos mais comprados dos ultimos 3 dia\n9.sair")
        print("#"*20)
        opcao = int(input("Opção -> "))

        if opcao == 9:
            break
        elif opcao == 1:
            mprod.cadastrar()
        elif opcao == 2:
            mprod.editar()
        elif opcao == 3:
            mprod.produtoSetor()
        elif opcao == 4:
            mprod.maisVendidos()


def MenuVenda():
    while True:
        limpaTela()
        print("#"*20)
        print("1.Nova Venda\n2.Listar Vendas do cliente\n9.Sair")
        print("#"*20)
        opcao = int(input("Opção -> "))

        if opcao == 9:
            break  # Retorna ao menu principal
        elif opcao == 1:
            # Chama função para realizar nova venda
            mvend.novaVenda()
        elif opcao == 2:
            # Chama função para listar vendas do cliente
            mvend.listarVendasCliente()


def MenuCliente():
    while True:
        limpaTela()
        print("#"*20)
        print(
            "1.Cadastrar novo cliente\n2.Atualizar pontuação\n3.Atualizar cliente\n9.Sair")
        print("#"*20)
        opcao = int(input("Opção -> "))
        if opcao == 9:
            break
        elif opcao == 1:
            mcli.cadastrarCli()
        elif opcao == 2:
            mcli.atualizarPontos()
        elif opcao == 3:
            mcli.editarCli()


def CadastrarProduto() -> dict:
    '''
    Exibe uma interface para ler os dados de um produto

    Retorno
    -------
    Retorno um dicionário com os campos e dados de um produto
    '''
    produto = {}
    print("="*30)
    print("Cadastro de um novo produto ")
    print("="*30)
    produto['Id'] = input("Identificação do produto: ")
    print("-"*30)
    produto['Setor'] = input("Setor do produto: ")
    print("-"*30)
    produto['Nome'] = input("Nome do produto: ")
    print("-"*30)
    produto['Preco'] = float(input("Preço do produto: "))
    print("-"*30)
    produto['Validade'] = input("Data de validade do produto: ")
    print("-"*30)
    produto['Quantidade'] = int(input("Quantidade de produto no estoque: "))
    print("="*30)
    return produto


def CadastrarClientes() -> dict:
    '''
    Exibe uma interface para ler os dados de um produto

    Retorno
    -------
    Retorno um dicionário com os campos e dados de um produto
    '''
    clientes = {}
    print("="*30)
    print("Cadastro de um novo Cliente ")
    print("="*30)
    clientes['CPF'] = input("Digite o cpf do cliente ?: ")
    print("-"*30)
    clientes['Nome'] = input("Digite o nome ")
    print("-"*30)
    clientes['Nascimento'] = (
        input("digite a data de nascimento ddmmyyyy: "))
    print("-"*30)
    clientes['Idade'] = int(input("digite idade: "))
    print("-"*30)
    clientes['Endereco'] = input("digite o endereço: ")
    print("-"*30)
    clientes['Cidade'] = input("digite a cidade: ")
    print("-"*30)
    clientes['Estado'] = input("digite a uf estado MT: ")
    print("-"*30)
    clientes['Pontos'] = 0
    print("="*30)
    return clientes


def EditarClientes() -> str:
    '''
    Exibe uma interface para ler o id do produto a ser editado

    Retorno
    -------
    Retorna o id do produto a ser editado
    '''
    print("="*30)
    print("Atualizar o Cliente ")
    print("="*30)
    cpf = input("CPF do cliente: ")
    print("="*30)
    return cpf


def EditarProduto() -> str:
    '''
    Exibe uma interface para ler o id do produto a ser editado

    Retorno
    -------
    Retorna o id do produto a ser editado
    '''
    print("="*30)
    print("Edição de um produto ")
    print("="*30)
    id = input("Identificação do produto: ")
    print("="*30)
    return id
