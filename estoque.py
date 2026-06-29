import os

estoque = []
ARQUIVO_TXT = "estoque_redes.txt"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_dados():
    try:
        with open(ARQUIVO_TXT, "w", encoding="utf-8") as arquivo:
            for item in estoque:
                linha = f"{item[0]};{item[1]};{item[2]};{item[3]};{item[4]};{item[5]}\n"
                arquivo.write(linha)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_dados():
    global estoque
    try:
        if os.path.exists(ARQUIVO_TXT):
            with open(ARQUIVO_TXT, "r", encoding="utf-8") as arquivo:
                estoque.clear()
                for linha in arquivo:
                    linha = linha.strip()
                    if linha:
                        dados = linha.split(";")
                        if len(dados) == 6:
                            estoque.append([
                                int(str(dados[0]).strip()), 
                                dados[1], 
                                dados[2], 
                                dados[3], 
                                float(str(dados[4]).strip()), 
                                int(str(dados[5]).strip())
                            ])
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

def cadastrar_rede():
    limpar_tela()
    print("### CADASTRAR NOVA REDE ###\n")
    try:
        codigo = int(input("Digite o código da rede: "))
    except ValueError:
        print("\n[ERRO] Código inválido!")
        input("\nPressione Enter para voltar...")
        return
    
    codigo_existe = False
    for item in estoque:
        if item[0] == codigo:
            codigo_existe = True
            break 

    if codigo_existe:
        print("\n[ERRO] Já existe uma rede com esse código!")
        input("\nPressione Enter para voltar...")
        return

    modelo = input("Digite o modelo da rede: ")
    cor = input("Digite a cor da rede: ")
    material = input("Digite o material da rede: ")
    
    try:
        preco = float(input("Digite o preço da rede: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
    except ValueError:
        print("\n[ERRO] Preço ou Quantidade inválidos!")
        input("\nPressione Enter para voltar...")
        return

    estoque.append([codigo, modelo, cor, material, preco, quantidade])
    salvar_dados()
    print("\nRede cadastrada com sucesso!")
    input("\nPressione Enter para voltar...")

def listar_redes():
    limpar_tela()
    if len(estoque) == 0:
        print("Nenhuma rede cadastrada.")
    else:
        print("=" * 82)
        print(f"{'LISTANDO TODAS AS REDES':^82}")
        print("=" * 82)
        print(f"{'CÓDIGO':<7} | {'MODELO':<20} | {'COR':<12} | {'MATERIAL':<12} | {'PREÇO':<12} | {'QTD':<6}")
        print("-" * 82)
        for item in estoque:
            preco_formatado = f"R$ {item[4]:.2f}"
            print(f"{item[0]:<7} | {item[1]:<20} | {item[2]:<12} | {item[3]:<12} | {preco_formatado:<12} | {item[5]:<6}")
        print("=" * 82)
    input("\nPressione Enter para voltar ao menu...")

def atualizar_rede():
    limpar_tela()
    try:
        codigo = int(input("Digite o código da rede que deseja alterar: "))
    except ValueError:
        print("\n[ERRO] Digite um número válido!")
        input("\nPressione Enter para voltar...")
        return

    for item in estoque:
        if item[0] == codigo:
            op = -1
            while op != 6:
                limpar_tela()
                print(f"Alterando Rede Código: {codigo}\n")
                print("""#####################################
###### O QUE DESEJA ALTERAR ? #######
#####################################
########## 1 - Modelo         #######
########## 2 - Cor            #######
########## 3 - Material       #######
########## 4 - Preço          #######
########## 5 - Quantidade     #######
########## 6 - Voltar         #######""")
                try:
                    op = int(input("Escolha: "))
                except ValueError:
                    print("\n[ERRO] Escolha inválida!")
                    input("Pressione Enter...")
                    continue

                if op == 1: 
                    item[1] = input("Novo modelo: ")
                elif op == 2: 
                    item[2] = input("Nova cor: ")
                elif op == 3: 
                    item[3] = input("Novo material: ")
                elif op == 4: 
                    try:
                        item[4] = float(input("Novo preço: "))
                    except ValueError:
                        print("\n[ERRO] Preço inválido! Alteração descartada.")
                        input("Pressione Enter...")
                elif op == 5: 
                    try:
                        item[5] = int(input("Nova quantidade: "))
                    except ValueError:
                        print("\n[ERRO] Quantidade inválida! Alteração descartada.")
                        input("Pressione Enter...")
                elif op == 6: 
                    print("\nAlterações finalizadas.")
                else: 
                    print("Opção inválida!")
            
            salvar_dados()
            input("\nPressione Enter para continuar...")
            return
    print("\nRede não encontrada.")
    input("\nPressione Enter para voltar...")

def buscar_rede():
    limpar_tela()
    try:
        codigo = int(input("Digite o código da rede: "))
    except ValueError:
        print("\n[ERRO] Código inválido!")
        input("\nPressione Enter para voltar...")
        return

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
            input("\nPressione Enter para voltar...")
            return
    print("\nRede não encontrada.")
    input("\nPressione Enter para voltar...")

def remover_rede():
    limpar_tela()
    try:
        codigo = int(input("Digite o código da rede que deseja remover: "))
    except ValueError:
        print("\n[ERRO] Código inválido!")
        input("\nPressione Enter para voltar...")
        return

    for item in estoque:
        if item[0] == codigo:
            confirmar = input("Tem certeza que deseja remover? [S/N]: ").upper()
            if confirmar == "S":
                estoque.remove(item)
                salvar_dados()
                print("\nRede removida com sucesso!")
            return
    print("\nRede não encontrada.")
    input("\nPressione Enter para voltar...")

def menu_estoque():
    carregar_dados()
    q = -1
    while q != 6:
        limpar_tela()
        print("""
###############################################
#       GERENCIAMENTO DE ESTOQUE              #
###############################################
######## 1 - CADASTRAR REDE          ##########
######## 2 - LISTAR REDES            ##########
######## 3 - ATUALIZAR REDE          ##########
######## 4 - BUSCAR REDE             ##########
######## 5 - REMOVER REDE            ##########
######## 6 - VOLTAR                  ##########""")
        try:
            q = int(input("Qual opção você deseja: "))
        except ValueError:
            print("\n[ERRO] Digite apenas números!")
            input("\nPressione Enter para continuar...")
            continue

        if q == 1: cadastrar_rede()
        elif q == 2: listar_redes()
        elif q == 3: atualizar_rede()
        elif q == 4: buscar_rede()
        elif q == 5: remover_rede()

if __name__ == "__main__":
    menu_estoque()