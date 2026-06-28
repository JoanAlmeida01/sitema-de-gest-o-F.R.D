
from estoque import estoque
from clientes import clientes

vendas = []

def nova_venda():
    cod_venda = int(input("Código da venda: "))
    cod_cliente = int(input("Código do cliente: "))
    
    cliente_existe = any(c[0] == cod_cliente for c in clientes)
    if not cliente_existe:
        print("Erro: Cliente não cadastrado no sistema!")
        return

    cod_produto = int(input("Código da rede: "))
    qtd = int(input("Quantidade: "))

    for item in estoque:
        if item[0] == cod_produto:
            if item[5] >= qtd:
                total = qtd * item[4]
                item[5] -= qtd
                vendas.append([cod_venda, cod_cliente, cod_produto, qtd, total])
                print("Venda realizada!")
                print(f"Total: R$ {total:.2f}")
            else:
                print("Estoque insuficiente.")
            return
    print("Produto não encontrado.")

def historico_vendas():
    if len(vendas) == 0:
        print("Nenhuma venda realizada.")
    else:
        for v in vendas:
            print(f"""
            Venda: {v[0]}
            Cliente: {v[1]}
            Produto: {v[2]}
            Quantidade: {v[3]}
            Total: R$ {v[4]:.2f}
            ------------------------""")

def buscar_venda():
    codigo = int(input("Código da venda: "))
    for v in vendas:
        if v[0] == codigo:
            print(f"\nVenda: {v[0]} | Cliente: {v[1]} | Produto: {v[2]} | Qtd: {v[3]} | Total: R$ {v[4]:.2f}")
            return
    print("Venda não encontrada.")

def menu_vendas():
    q = -1
    while q != 4:
        print("""
###############################################
######## 1 - NOVA VENDA             ###########
######## 2 - HISTÓRICO DE VENDAS    ###########
######## 3 - BUSCAR VENDA           ###########
######## 4 - VOLTAR                 ###########""")
        q = int(input("Qual opção você deseja: "))
        if q == 1: nova_venda()
        elif q == 2: historico_vendas()
        elif q == 3: buscar_venda()
        elif q != 4: print("Opção inválida!")