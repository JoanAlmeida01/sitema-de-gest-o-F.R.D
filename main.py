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

# --- INICIALIZAÇÃO E CARREGAMENTO DOS DADOS ---
# Certifique-se de que essas funções existem com esses nomes nos seus módulos.
# Elas lêem os arquivos .txt e preenchem as listas 'estoque' e 'clientes'.
try:
    estoque.carregar_dados()  # Substitua pelo nome correto da função se for diferente
    clientes.carregar_dados() # Substitua pelo nome correto da função se for diferente
except AttributeError:
    # Caso suas funções tenham outros nomes em estoque.py ou clientes.py, 
    # o Python avisará aqui sem travar o início do programa
    print("[AVISO] Não foi possível carregar os dados automaticamente. Verifique os nomes das funções de leitura.")
    input("Pressione Enter para continuar...")

resp = -1
while resp != 0:
    limpar_tela()
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