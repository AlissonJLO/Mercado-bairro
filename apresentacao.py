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
            "1.Cadastrar novo produto\n2.Atualizar imformaçoes do produto\n3.Estoque por setor\n4.produtos com estoque baixo\n5.produtos mais vendidos\n9.sair")
        print("#"*20)
        opcao = int(input("Opção -> "))

        if opcao == 9:
            break
        elif opcao == 1:
            mprod.cadastrar()
        elif opcao == 2:
            mprod.editar()
        elif opcao == 3:
            mprod.estoqueSetor()
        elif opcao == 4:
            mprod.estoqueBaixo()
        elif opcao == 5:
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


def MenuCliente() -> str:
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
            mcli.cadastrar()
        elif opcao == 2:
            mcli.atualizarPontos()
        elif opcao == 3:
            mcli.atualizarCliente()


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
