from os import system, name

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


def MenuProduto() -> str:
    opcoes = [1, 2, 3, 4, 5, 9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print(
            "1.Cadastrar novo produto\n2.Atualizar informações do produto\n3.Estoque por setor\n4.Produtos com estoque baixo\n5.Produtos mais vendidos\n9.Sair")
        print("#"*20)
        opcao = int(input("Opção -> "))


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


def EditarProduto() -> int:
    '''
    Exibe uma interface para ler o id do produto a ser editado

    Retorno
    -------
    Retorna o id do produto a ser editado
    '''
    print("="*30)
    print("Edição de um produto ")
    print("="*30)
    id = int(input("Identificação do produto: "))
    print("="*30)
    return id
