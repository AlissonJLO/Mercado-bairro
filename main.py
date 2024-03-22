import apresentacao


def main():
    while True:
        opcao = apresentacao.MenuPrincipal()
        if opcao == 9:
            print("Saindo do programa...")
            break
        elif opcao == 1:
            apresentacao.MenuVenda()
        elif opcao == 2:
            apresentacao.MenuCliente()
        elif opcao == 3:
            apresentacao.MenuProduto()


# Inicio do programa
if __name__ == "__main__":
    main()
