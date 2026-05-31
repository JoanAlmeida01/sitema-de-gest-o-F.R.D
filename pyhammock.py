resp = -1

while resp != 0:

    print("#" * 35)
    print("### SISTEMA DE REDES DE DORMIR ###")
    print("#" * 35)

    print("""
#####################################
######## 1 - ESTOQUE       ##########
######## 2 - CLIENTES      ##########
######## 3 - VENDAS        ##########
######## 4 - RELATÓRIOS    ##########
######## 5 - INFORMAÇÕES   ##########
######## 0 - SAIR          ##########
#####################################
""")

    resp = int(input("Qual opção você deseja: "))

    # ESTOQUE
    if resp == 1:

        op = -1

        while op != 6:

            print("""
###############################################
###        GERENCIAMENTO DE ESTOQUE         ###
###############################################
######## 1 - CADASTRAR REDE          ##########
######## 2 - LISTAR REDES            ##########
######## 3 - ATUALIZAR REDE          ##########
######## 4 - BUSCAR REDE             ##########
######## 5 - REMOVER REDE            ##########
######## 6 - VOLTAR                  ##########
###############################################
""")

            op = int(input("Qual opção você deseja: "))

            if op == 1:
                pass

            elif op == 2:
                pass

            elif op == 3:
                pass

            elif op == 4:
                pass

            elif op == 5:
                pass

    # CLIENTES
    elif resp == 2:

        op = -1

        while op != 6:

            print("""
###############################################
###        GERENCIAMENTO DE CLIENTES        ###
###############################################
######## 1 - CADASTRAR CLIENTE       ##########
######## 2 - LISTAR CLIENTES         ##########
######## 3 - ATUALIZAR CLIENTE       ##########
######## 4 - BUSCAR CLIENTE          ##########
######## 5 - REMOVER CLIENTE         ##########
######## 6 - VOLTAR                  ##########
###############################################
""")

            op = int(input("Qual opção você deseja: "))

            if op == 1:
                pass

            elif op == 2:
                pass

            elif op == 3:
                pass

            elif op == 4:
                pass

            elif op == 5:
                pass

    # VENDAS
    elif resp == 3:

        op = -1

        while op != 5:

            print("""
###############################################
###         GERENCIAMENTO DE VENDAS         ###    
###############################################
######## 1 - NOVA VENDA             ###########
######## 2 - LISTAR VENDAS          ###########
######## 3 - BUSCAR VENDA           ###########
######## 4 - CANCELAR VENDA         ###########
######## 5 - VOLTAR                 ###########
###############################################
""")

            op = int(input("Qual opção você deseja: "))

            if op == 1:
                pass

            elif op == 2:
                pass

            elif op == 3:
                pass

            elif op == 4:
                pass

    # RELATÓRIOS
    elif resp == 4:

        op = -1

        while op != 5:

            print("""
###############################################
###          RELATÓRIOS                     ###
###############################################
######## 1 - TOTAL DE VENDAS        ###########
######## 2 - TOTAL EM ESTOQUE       ###########
######## 3 - CLIENTES CADASTRADOS   ###########
######## 4 - PRODUTO MAIS VENDIDO   ###########
######## 5 - VOLTAR                 ###########
###############################################
""")

            op = int(input("Qual opção você deseja: "))

            if op == 1:
                pass

            elif op == 2:
                pass

            elif op == 3:
                pass

            elif op == 4:
                pass

    # INFORMAÇÕES
    elif resp == 5:

        print("""
###############################################
###          INFORMAÇÕES                    ###
###############################################
Projeto: Sistema de Gestão de Redes
Disciplina: Programação
Versão: 1.0
""")

    elif resp == 0:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")