estoque = []

def cadastrar_rede():
    codigo = int(input("Digite o código da rede: "))
    modelo = input("Digite o modelo da rede: ")
    cor = input("Digite a cor da rede: ")
    material = input("Digite o material da rede: ")
    preco = float(input("Digite o preço da rede: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    estoque.append([codigo, modelo, cor, material, preco, quantidade])
    print("Rede cadastrada com sucesso!")

def listar_redes():
    if len(estoque) == 0:
        print("Nenhuma rede cadastrada.")
    else:
        print("\nLISTANDO TODAS AS REDES...\n")
        for item in estoque:
            print(f"""
            CÓDIGO: {item[0]}
            MODELO: {item[1]}
            COR: {item[2]}
            MATERIAL: {item[3]}
            PREÇO: R$ {item[4]:.2f}
            QUANTIDADE: {item[5]}
            --------------------------------""")

def atualizar_rede():
    codigo = int(input("Digite o código da rede: "))
    for item in estoque:
        if item[0] == codigo:
            op = -1
            while op != 6:
                print("""
#####################################
###### O QUE DESEJA ALTERAR ? #######
#####################################
########## 1 - Modelo         #######
########## 2 - Cor            #######
########## 3 - Material       #######
########## 4 - Preço          #######
########## 5 - Quantidade     #######
########## 6 - Voltar         #######""")
                op = int(input("Escolha: "))
                if op == 1: item[1] = input("Novo modelo: ")
                elif op == 2: item[2] = input("Nova cor: ")
                elif op == 3: item[3] = input("Novo material: ")
                elif op == 4: item[4] = float(input("Novo preço: "))
                elif op == 5: item[5] = int(input("Nova quantidade: "))
                elif op == 6: print("Alterações finalizadas.")
                else: print("Opção inválida!")
            return
    print("Rede não encontrada.")

def buscar_rede():
    codigo = int(input("Digite o código da rede: "))
    for item in estoque:
        if item[0] == codigo:
            print(f"""
            ### REDE ENCONTRADA ###
            CÓDIGO: {item[0]}
            MODELO: {item[1]}
            COR: {item[2]}
            MATERIAL: {item[3]}
            PREÇO: R$ {item[4]:.2f}
            QUANTIDADE: {item[5]}""")
            return
    print("Rede não encontrada.")

def remover_rede():
    codigo = int(input("Digite o código da rede que deseja remover: "))
    for item in estoque:
        if item[0] == codigo:
            confirmar = input("Tem certeza que deseja remover? [S/N]: ").upper()
            if confirmar == "S":
                estoque.remove(item)
                print("Rede removida com sucesso!")
            return
    print("Rede não encontrada.")

def menu_estoque():
    q = -1
    while q != 6:
        print("""
###############################################
#         GERENCIAMENTO DE ESTOQUE            #
###############################################
######## 1 - CADASTRAR REDE          ##########
######## 2 - LISTAR REDES            ##########
######## 3 - ATUALIZAR REDE          ##########
######## 4 - BUSCAR REDE             ##########
######## 5 - REMOVER REDE            ##########
######## 6 - VOLTAR                  ##########""")
        q = int(input("Qual opção você deseja: "))
        if q == 1: cadastrar_rede()
        elif q == 2: listar_redes()
        elif q == 3: atualizar_rede()
        elif q == 4: buscar_rede()
        elif q == 5: remover_rede()
        elif q != 6: print("Opção inválida!")