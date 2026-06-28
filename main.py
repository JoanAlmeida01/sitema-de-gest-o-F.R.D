import estoque
import clientes
import vendas
import relatorios

def exibir_informacoes():
    print("""
###################################################
##########      MÓDULO INFORMAÇÕES       ##########
###################################################
###################################################
### PROJETO DE PROGRAMAÇÃO EM PYTHON            ###
### TEMA: SISTEMA DE REDES DE DORMIR            ###
### DISCENTE: Joan Almeida                      ###
###################################################""")

resp = -1
while resp != 0:
    print("#" * 35)
    print("### SISTEMA DE REDES DE DORMIR ###")
    print("#" * 35)
    print("""
###############################################
######## 1 - GERENCIAR ESTOQUE       ##########
######## 2 - GERENCIAR CLIENTES      ##########
######## 3 - GERENCIAR VENDAS        ##########
######## 4 - RELATÓRIOS              ##########
######## 5 - INFORMAÇÕES             ##########
######## 0 - SAIR                    ##########""")

    resp = int(input("Qual opção você deseja: "))

    if resp == 1: estoque.menu_estoque()
    elif resp == 2: clientes.menu_clientes()
    elif resp == 3: vendas.menu_vendas()
    elif resp == 4: relatorios.menu_relatorios()
    elif resp == 5: exibir_informacoes()
    elif resp == 0:
        print("\n#################################\n##### PROGRAMA ENCERRADO ########\n#################################")
    else:
        print("OPÇÃO INVÁLIDA!")