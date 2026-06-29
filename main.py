import os
import estoque
import clientes
import vendas
import relatorios

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_informacoes():
    limpar_tela()
    print("""
###################################################
##########      MÓDULO INFORMAÇÕES       ##########
###################################################
###################################################
### PROJETO DE PROGRAMAÇÃO EM PYTHON            ###
### TEMA: SISTEMA DE REDES DE DORMIR            ###
### DISCENTE: Joan Almeida                      ###
###################################################""")
    input("\nPressione Enter para voltar ao menu principal...")

try:
    estoque.carregar_dados()  
    clientes.carregar_dados() 
except AttributeError:
    print("[AVISO] Não foi possível carregar os dados automaticamente. Verifique os nomes das funções de leitura.")
    input("Pressione Enter para continuar...")

resp = -1
while resp != 0:
    limpar_tela()
    print("#" * 96)
    print(r""" _  _   __   _  _  _  _   __    ___  __ _    __  __ _  _  _  ____  __ _  ____  __  ____  _  _       
/ )( \ / _\ ( \/ )( \/ ) /  \  / __)(  / )  (  )(  ( \/ )( \(  __)(  ( \(_  _)/  \(  _ \( \/ )      
) __ (/    \/ \/ \/ \/ \(  O )( (__  )  (    )( /    /\ \/ / ) _) /    /  )( (  O ))   / )  /       
\_)(_/\_/\_/\_)(_/\_)(_/ \__/  \___)(__\_)  (__)\_)__) \__/ (____)\_)__) (__) \__/(__\_)(__/        
                         ____  _  _  ____  ____  ____  _  _                                         
                        / ___)( \/ )/ ___)(_  _)(  __)( \/ )                                        
                        \___ \ )  / \___ \  )(   ) _) / \/ \                                        
                        (____/(__/  (____/ (__) (____)\_)(_/                                         """) 
    print("#" * 96)
    print("""                   ###############################################
                   ######## 1 - GERENCIAR ESTOQUE       ##########
                   ######## 2 - GERENCIAR CLIENTES      ##########
                   ######## 3 - GERENCIAR VENDAS        ##########
                   ######## 4 - RELATÓRIOS              ##########
                   ######## 5 - INFORMAÇÕES             ##########
                   ######## 0 - SAIR                    ##########""")

    try:
        resp = int(input("Qual opção você deseja: "))
    except ValueError:
        print("\n[ERRO] Por favor, digite apenas números!")
        input("\nPressione Enter para continuar...")
        resp = -1
        continue 

    if resp == 1: 
        estoque.menu_estoque()
    elif resp == 2: 
        clientes.menu_clientes()
    elif resp == 3: 
        vendas.menu_vendas()
    elif resp == 4: 
        relatorios.menu_relatorios()
    elif resp == 5: 
        exibir_informacoes()
    elif resp == 0:
        limpar_tela()
        print("\n#################################\n##### PROGRAMA ENCERRADO ########\n#################################\n")
    else:
        print("\nOPÇÃO INVÁLIDA!\n")
        input("Pressione Enter para continuar...")