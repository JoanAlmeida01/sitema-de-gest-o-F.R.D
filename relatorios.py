import os
from vendas import vendas, carregar_vendas

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def relatorio_faturamento():
    limpar_tela()
    total_faturado = sum(venda[4] for venda in vendas)
    print(f"\n=====================================")
    print(f"TOTAL FATURADO DOS PRODUTOS: R$ {total_faturado:.2f}")
    print(f"=====================================")
    input("\nPressione Enter para voltar...")

def relatorio_rede_mais_vendida():
    limpar_tela()
    if len(vendas) == 0:
        print("Nenhuma venda cadastrada.")
    else:
        produto = {}
        for venda in vendas:
            produto[venda[2]] = produto.get(venda[2], 0) + venda[3]
        
        codigo_produto = max(produto, key=produto.get)
        mais_vendido = produto[codigo_produto]
        print(f"=====================================")
        print(f"REDE MAIS VENDIDA (CÓDIGO): {codigo_produto}")
        print(f"QUANTIDADE VENDIDA: {mais_vendido} unidades")
        print(f"=====================================")
    input("\nPressione Enter para voltar...")

def relatorio_cliente_mais_compra():
    limpar_tela()
    if len(vendas) == 0:
        print("Nenhuma venda cadastrada.")
    else:
        clientes_compra = {}
        for venda in vendas:
            clientes_compra[venda[1]] = clientes_compra.get(venda[1], 0) + venda[3]
        
        melhor_cliente = max(clientes_compra, key=clientes_compra.get)
        maior = clientes_compra[melhor_cliente]
        print(f"=====================================")
        print(f"CLIENTE QUE MAIS COMPRA (CÓDIGO): {melhor_cliente}")
        print(f"TOTAL DE ITENS COMPRADOS: {maior} itens")
        print(f"=====================================")
    input("\nPressione Enter para voltar...")

def menu_relatorios():
    carregar_vendas() 
    q = -1
    while q != 5:
        limpar_tela()
        print("""
###################################################
############ 1 - TOTAL FATURADO            ########
############ 2 - REDE MAIS VENDIDA         ########
############ 3 - CLIENTES QUE MAIS COMPRAM ########
############ 4 - QUANTIDADE DE VENDAS      ########
############ 5 - VOLTAR                    ########""")
        try:
            q = int(input("Qual opção você deseja: "))
        except ValueError:
            print("\n[ERRO] Digite apenas números!")
            input("\nPressione Enter para continuar...")
            continue

        if q == 1: relatorio_faturamento()
        elif q == 2: relatorio_rede_mais_vendida()
        elif q == 3: relatorio_cliente_mais_compra()
        elif q == 4: 
            limpar_tela()
            print(f"=====================================")
            print(f"QUANTIDADE DE VENDAS REALIZADAS: {len(vendas)}")
            print(f"=====================================")
            input("\nPressione Enter para voltar...")