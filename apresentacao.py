from os import system, name
import manipulaClientes as mcli
import manipulaProduto as mprod
import manipulaVenda as mvend
import manipulaItensCompra as mitc
from datetime import datetime
import re
import time

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
            break
         # Retorna ao menu principal
        elif opcao == 1:
            # Chama função para realizar nova venda
            mvend.novaVenda()
        elif opcao == 2:
            # Chama função para listar vendas do cliente
            mvend.listarVendas()


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
    setoresValidos = ["Higiene", "Limpeza",
                      "Bebidas", "Frios", "Padaria", "Açougue"]
    produto = {}
    produtos = mprod.carregar()
    print("="*30)
    print("Cadastro de um novo produto ")
    print("="*30)
    produto['Id-Produto'] = str(len(produtos) + 1)
    print("-"*30)
    produto['Setor'] = input("Setor do produto: ")
    while produto['Setor'] not in setoresValidos:
        print("-"*30)
        print("Setor inválido. Setores válidos: Higiene, Limpeza, Bebidas, Frios, Padaria, Açougue")
        produto['Setor'] = input("Setor do produto: ")
    print("-"*30)
    produto['Nome'] = input("Nome do produto: ")
    print("-"*30)
    produto['Preco'] = float(input("Preço do produto: "))
    print("-"*30)
    while True:
        validade = input("Digite a data de validade dd/mm/yyyy: ")
        if validar_data(validade):
            produto['Validade'] = validade
            break
        else:
            print("Data inválida, por favor, digite novamente no formato dd/mm/yyyy.")
    print("-"*30)
    produto['Quantidade'] = int(input("Quantidade de produto no estoque: "))
    print("="*30)
    return produto


def validar_data(data):
    '''
    Valida se a string de nascimento está no formato dd/mm/aaaa e é uma data válida.

    Parâmetros
    ----------
    nascimento : str
        A string da data de nascimento a ser validada.

    Retorno
    -------
    bool
        Retorna True se a data for válida, False caso contrário.
    '''
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def calcular_idade(nascimento):
    '''
    Calcula a idade baseado na data de nascimento.

    Parâmetros
    ----------
    nascimento : str
        A data de nascimento no formato dd/mm/yyyy.

    Retorno
    -------
    int
        A idade calculada a partir da data de nascimento.
    '''
    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - \
        ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade


def CadastrarClientes() -> dict:
    '''
    Exibe uma interface para ler os dados de um cliente

    Retorno
    -------
    Retorna um dicionário com os campos e dados de um cliente.
    '''
    clientes = {}
    print("="*30)
    print("Cadastro de um novo Cliente")
    print("="*30)
    # Supõe-se que ler_cpf é uma função definida em outro lugar do código
    clientes['CPF'] = ler_cpf()
    print("-"*30)
    clientes['Nome'] = input("Digite o nome: ")
    print("-"*30)

    # Validação da data de nascimento e cálculo da idade
    while True:
        nascimento = input("Digite a data de nascimento dd/mm/yyyy: ")
        # Supõe-se que validar_data é uma função definida em outro lugar do código
        if validar_data(nascimento):
            clientes['Nascimento'] = nascimento
            clientes['Idade'] = calcular_idade(nascimento)
            break
        else:
            print("Data inválida, por favor, digite novamente no formato dd/mm/yyyy.")

    print("-"*30)
    print(f"Idade calculada: {clientes['Idade']} anos")
    print("-"*30)
    clientes['Endereco'] = input("Digite o endereço: ")
    print("-"*30)
    clientes['Cidade'] = input("Digite a cidade: ")
    print("-"*30)
    clientes['Estado'] = input("Digite a UF: ")
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


def validar_formato_cpf(cpf: str) -> bool:
    """
    Verifica se o formato do CPF é válido (XXX.XXX.XXX-XX).
    """
    # Padrão de regex para validar o formato do CPF
    pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(pattern, cpf) is not None


def ler_cpf() -> str:
    '''
    Exibe uma interface para inserir o CPF no formato xxx.xxx.xx-xx
    e verifica se foi digitado corretamente.

    Retorno
    -------
    Retorna o CPF no formato correto se validado, caso contrário,
    solicita novamente.
    '''
    while True:
        limpaTela()
        cpf = input("CPF do cliente (XXX.XXX.XXX-XX): ").strip()
        # Verifica o formato do CPF
        if not validar_formato_cpf(cpf):
            print(
                "Formato de CPF inválido. Por favor, digite novamente no formato XXX.XXX.XXX-XX.")
            time.sleep(2)
            continue

        print("="*30)
        print(f"Confirme o CPF: {cpf}\n")
        print("="*30)
        print("1. CPF correto\n2. CPF incorreto\n")
        try:
            opcao = int(input("Opção -> "))
            if opcao == 1:
                return cpf
            elif opcao == 2:
                continue
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número válido.")
        time.sleep(5)


def exibirProduto(id_produto: str):
    '''
    Exibe as informações de um produto a partir do ID fornecido
    ------------
    retorna produto

    '''
    produtos = mprod.carregar()
    for produto in produtos:
        if produto['Id-Produto'] == id_produto:
            print(f"ID: {produto['Id-Produto']}")
            print(f"Nome: {produto['Nome']}")
            print(f"Setor: {produto['Setor']}")
            print(f"Preço: R$ {produto['Preco']}")
            print(f"Validade: {produto['Validade']}")
            print(f"Quantidade em estoque: {produto['Quantidade']}")
            return produto
    else:
        print("Produto não encontrado.")
        return False


def efetuar_venda() -> dict:
    '''
    inicia uma venda
    ------
    retorna venda
    '''
    clientes = mcli.carregar()
    cpf = ler_cpf()
    if not mcli.checar_cadastro(clientes, cpf):
        print("Cliente não cadastrado.")
        print("Redirecionando para cadastro...")
        cpf = mcli.cadastrarCli()
        limpaTela()
    vendas = mvend.carregar()
    itensCompra = mitc.carregar()
    listaItens = []
    quantidadeProdutos = 0
    idVenda = len(vendas) + 1

    while True:
        id_produto = input("Digite o ID do produto (ou 'x' para encerrar): ")
        if id_produto.lower() == 'x':
            itensCompra.extend(listaItens)
            total = 0
            for item in listaItens:
                total += float(item['Preco-Total'])
            if quantidadeProdutos != 0:
                vendas.append(
                    {"Id-Venda": idVenda, "CPF": cpf, "Data": datetime.now().strftime("%d/%m/%Y"), "Total": total, "Quantidade-Produtos": quantidadeProdutos})
            return {
                'itensCompra': itensCompra,
                'vendas': vendas,
            }
        else:
            produto = exibirProduto(id_produto)
            if not produto:
                print("Produto não encontrado.")
            elif int(produto['Quantidade']) == 0:
                print("Não há quantidade disponível do produto")
            else:
                quantidade = int(input("Digite a quantidade de itens: "))
                if quantidade > int(produto['Quantidade']):
                    print(
                        f"Quantidade insuficiente em estoque. Disponível: {produto['Quantidade']}")
                else:
                    preco_total = float(produto['Preco']) * quantidade
                    listaItens.append(
                        {"Id-Venda": idVenda, 'CPF': cpf, "Id-Produto": produto['Id-Produto'], "Quantidade": quantidade, "Preco-Unitario": produto['Preco'], "Preco-Total": preco_total})
                    mvend.BaixaEstoque(id_produto, quantidade)
                    quantidadeProdutos += 1


def listar_vendas():
    limpaTela()
    print("="*30)
    print('Digite o método de pesquisa\n 1.CPF\n 2.Nome completo\n')
    opcao = int(input("Opção -> "))

    vendas = mvend.carregar()  # Carregar vendas uma única vez

    if opcao == 1:
        cpf = ler_cpf()  # Supondo que ler_cpf() é uma função que você já tem
        for venda in vendas:
            if venda['CPF'] == cpf:
                print(f"ID da venda: {venda['Id-Venda']}")
                print(f"Data da venda: {venda['Data']}")
                print(f"Total da venda: R$ {venda['Total']}")
                print(
                    f"Quantidade de produtos: {venda['Quantidade-Produtos']}")
                print("="*30)
        input("Pressione Enter para continuar...")
    elif opcao == 2:
        nome = input("Digite o nome completo do cliente: ")
        clientes = mcli.carregar()  # Supondo que mcli.carregar() carrega todos os clientes

        cpf_encontrado = None
        for cliente in clientes:
            if cliente['Nome'] == nome:
                cpf_encontrado = cliente['CPF']
                break  # Neste ponto, podemos interromper o loop porque encontramos o CPF do cliente pelo nome

        if cpf_encontrado:
            for venda in vendas:
                if venda['CPF'] == cpf_encontrado:
                    print(f"ID da venda: {venda['Id-Venda']}")
                    print(f"Data da venda: {venda['Data']}")
                    print(f"Total da venda: R$ {venda['Total']}")
                    print(
                        f"Quantidade de produtos: {venda['Quantidade-Produtos']}")
                    print("="*30)
            input("Pressione Enter para continuar...")
        else:
            print("Cliente não encontrado.")

    else:
        print("Opção inválida.")

# Id-Venda;CPF;Id-Produto;Quantidade;Preço-Unitário;Preço-Total
# Id-Venda;CPF;Data;Total;Quantidade-Produtos
