produtos = []

while True:
    print("\n========== MENU ==========")
    print("1 - Cadastrar Rede")
    print("2 - Listar Redes")
    print("3 - Atualizar Estoque")
    print("4 - Realizar Venda")
    print("5 - Relatório")
    print("0 - Sair")
    print("==========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = input("Código da rede: ")
        nome = input("Nome da rede: ")
        preco = float(input("Preço (R$): "))
        estoque = int(input("Quantidade em estoque: "))
        produtos.append([codigo, nome, preco, estoque])
        print("Rede cadastrada com sucesso!")