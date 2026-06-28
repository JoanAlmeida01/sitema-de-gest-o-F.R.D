clientes = []

def cadastrar_cliente():
    codigo = int(input("Código: "))
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")
    clientes.append([codigo, nome, telefone, cidade])
    print("Cliente cadastrado!")

def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            print(f"""
            Código: {c[0]}
            Nome: {c[1]}
            Telefone: {c[2]}
            Cidade: {c[3]}
            -------------------------""")

def buscar_cliente():
    codigo = int(input("Digite o código: "))
    for c in clientes:
        if c[0] == codigo:
            print(f"\nCódigo: {c[0]} | Nome: {c[1]} | Telefone: {c[2]} | Cidade: {c[3]}")
            return
    print("Cliente não encontrado.")

def atualizar_cliente():
    codigo = int(input("Código do cliente: "))
    for c in clientes:
        if c[0] == codigo:
            c[1] = input("Novo nome: ")
            c[2] = input("Novo telefone: ")
            c[3] = input("Nova cidade: ")
            print("Cliente atualizado!")
            return
    print("Cliente não encontrado.")

def remover_cliente():
    codigo = int(input("Digite o código do cliente que deseja remover: "))
    for c in clientes:
        if c[0] == codigo:
            confirmar = input("Tem certeza que deseja remover? [S/N]: ").upper()
            if confirmar == "S":
                clientes.remove(c)
                print("Cliente removido com sucesso!")
            return
    print("Cliente não encontrado.")

def menu_clientes():
    q = -1
    while q != 6:
        print("""
###############################################
######## 1 - CADASTRAR CLIENTE       ##########
######## 2 - LISTAR CLIENTES         ##########
######## 3 - BUSCAR CLIENTE          ##########
######## 4 - ATUALIZAR CLIENTE       ##########
######## 5 - REMOVER CLIENTE         ##########
######## 6 - VOLTAR                  ##########""")
        try:
            q = int(input("Qual opção você deseja: "))
        except ValueError:
            print("\n[ERRO] Por favor, digite apenas números!")
            q = -1
            continue 
        if q == 1: cadastrar_cliente()
        elif q == 2: listar_clientes()
        elif q == 3: buscar_cliente()
        elif q == 4: atualizar_cliente()
        elif q == 5: remover_cliente()
        elif q != 6: print("Opção inválida!")