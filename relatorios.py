from vendas import vendas

def relatorio_faturamento():
    total_faturado = sum(venda[4] for venda in vendas)
    print(f"\nTOTAL FATURADO: R$ {total_faturado:.2f}")

def relatorio_rede_mais_vendida():
    if len(vendas) == 0:
        print("Nenhuma venda cadastrada.")
        return
    produto = {}
    for venda in vendas:
        produto[venda[2]] = produto.get(venda[2], 0) + venda[3]
    
    codigo_produto = max(produto, key=produto.get)
    mais_vendido = produto[codigo_produto]
    print(f"REDE MAIS VENDIDA (CÓDIGO): {codigo_produto}\nQUANTIDADE VENDIDA: {mais_vendido}")

def relatorio_cliente_mais_compra():
    if len(vendas) == 0:
        print("Nenhuma venda cadastrada.")
        return
    clientes_compra = {}
    for venda in vendas:
        clientes_compra[venda[1]] = clientes_compra.get(venda[1], 0) + venda[3]
    
    melhor_cliente = max(clientes_compra, key=clientes_compra.get)
    maior = clientes_compra[melhor_cliente]
    print(f"CLIENTE QUE MAIS COMPRA (CÓDIGO): {melhor_cliente}\nTOTAL DE ITENS COMPRADOS: {maior}")

def menu_relatorios():
    q = -1
    while q != 5:
        print("""
###################################################
############ 1 - TOTAL FATURADO            ########
############ 2 - REDE MAIS VENDIDA         ########
############ 3 - CLIENTES QUE MAIS COMPRAM ########
############ 4 - QUANTIDADE DE VENDAS      ########
############ 5 - VOLTAR                    ########""")
        q = int(input("Qual opção você deseja: "))
        if q == 1: relatorio_faturamento()
        elif q == 2: relatorio_rede_mais_vendida()
        elif q == 3: relatorio_cliente_mais_compra()
        elif q == 4: print(f"QUANTIDADE DE VENDAS REALIZADAS: {len(vendas)}")
        elif q != 5: print("Opção inválida!")