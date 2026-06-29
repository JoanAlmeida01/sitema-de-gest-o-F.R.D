import os
from estoque import estoque, salvar_dados as salvar_estoque
# IMPORTANTE: Agora importamos a lista AND a função de salvar do módulo clientes
from clientes import clientes, salvar_clientes 

vendas = []
ARQUIVO_VENDAS = "historico_vendas.txt"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_cpf(cpf: str) -> bool:
    cpf = "".join(char for char in cpf if char.isdigit())

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito_1 = 0 if resto == 10 else resto

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito_2 = 0 if resto == 10 else resto

    return cpf[9] == str(digito_1) and cpf[10] == str(digito_2)

def salvar_vendas():
    try:
        with open(ARQUIVO_VENDAS, "w", encoding="utf-8") as arquivo:
            for v in vendas:
                linha = f"{v[0]};{v[1]};{v[2]};{v[3]};{v[4]}\n"
                arquivo.write(linha)
    except Exception as e:
        print(f"Erro ao salvar vendas: {e}")

def carregar_vendas():
    global vendas
    vendas.clear()
    try:
        with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    dados = linha.split(";")
                    vendas.append([int(dados[0]), dados[1], int(dados[2]), int(dados[3]), float(dados[4])])
    except FileNotFoundError:
        pass

def nova_venda():
    limpar_tela()
    print("### NOVA VENDA ###\n")
    cod_venda = int(input("Código da venda: "))
    
    if any(v[0] == cod_venda for v in vendas):
        print("\n[ERRO] Já existe uma venda com este código!")
        input("\nPressione Enter para voltar...")
        return

    opcao_cadastro = input("O cliente deseja informar o CPF para a venda? [S/N]: ").strip().upper()
    
    if opcao_cadastro == "S":
        cpf = input("Digite o CPF do cliente (apenas números ou formatado): ").strip()
        identificador_cliente = "".join(char for char in cpf if char.isdigit())
        
        if not validar_cpf(identificador_cliente):
            print("\n[ERRO] CPF inválido!")
            input("\nPressione Enter para voltar...")
            return
            
        if not any(c[0] == identificador_cliente for c in clientes):
            print("\n[AVISO] CPF não cadastrado no sistema!")
            opcao = input("Deseja cadastrar este cliente agora? [S/N]: ").strip().upper()
            
            if opcao == "S":
                print("\n--- CADASTRO DE CLIENTE ---")
                nome = input("Nome do cliente: ")
                telefone = input("Telefone: ")
                cidade = input("Cidade: ")
                
                # Adiciona o novo cliente na lista global de clientes
                clientes.append([identificador_cliente, nome, telefone, cidade])
                
                # CORREÇÃO AQUI: Chama a função que grava fisicamente no 'clientes.txt'
                salvar_clientes()
                
                print("\n[SUCESSO] Cliente cadastrado no sistema! Continuando com a venda...")
                input("Pressione Enter para continuar...")
            else:
                print("\nVenda cancelada pois o cliente não foi cadastrado.")
                input("\nPressione Enter para voltar...")
                return
    else:
        print("\nColetando dados simplificados do cliente:")
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        cidade = input("Cidade: ")
        identificador_cliente = f"Sem CPF ({nome})"

    # Coleta de informações do produto
    cod_produto = int(input("Código da rede (produto): "))
    qtd = int(input("Quantidade: "))

    for item in estoque:
        try:
            codigo_estoque = int(str(item[0]).strip())
        except (ValueError, IndexError):
            continue

        if codigo_estoque == cod_produto:
            preco_unitario = float(str(item[4]).strip())
            qtd_estoque = int(str(item[5]).strip())

            if qtd_estoque >= qtd:
                total = qtd * preco_unitario
                item[5] = qtd_estoque - qtd
                
                vendas.append([cod_venda, identificador_cliente, cod_produto, qtd, total])
                salvar_vendas()
                salvar_estoque()
                
                print(f"\nVenda realizada! Produto: {item[1]} | Total: R$ {total:.2f}")
            else:
                print(f"\nEstoque insuficiente. Disponível: {qtd_estoque}")
            input("\nPressione Enter para voltar...")
            return
            
    print("\nProduto não encontrado.")
    input("\nPressione Enter para voltar...")

def historico_vendas():
    limpar_tela()
    if len(vendas) == 0:
        print("Nenhuma venda realizada.")
    else:
        print("=" * 80)
        print(f"{'HISTÓRICO DE VENDAS':^80}")
        print("=" * 80)
        print(f"{'VENDA':<7} | {'CLIENTE / IDENTIFICADOR':<25} | {'PRODUTO':<9} | {'QTD':<5} | {'TOTAL':<12}")
        print("-" * 80)
        for v in vendas:
            if v[1].isdigit() and len(v[1]) == 11:
                cliente_exibicao = f"{v[1][:3]}.{v[1][3:6]}.{v[1][6:9]}-{v[1][9:]}"
            else:
                cliente_exibicao = v[1]
                
            print(f"{v[0]:<7} | {cliente_exibicao:<25} | {v[2]:<9} | {v[3]:<5} | R$ {v[4]:.2f}")
        print("=" * 80)
    input("\nPressione Enter para voltar...")

def buscar_venda():
    limpar_tela()
    codigo = int(input("Código da venda: "))
    for v in vendas:
        if v[0] == codigo:
            if v[1].isdigit() and len(v[1]) == 11:
                cliente_exibicao = f"{v[1][:3]}.{v[1][3:6]}.{v[1][6:9]}-{v[1][9:]}"
            else:
                cliente_exibicao = v[1]
                
            print(f"\nVenda: {v[0]} | Cliente: {cliente_exibicao} | Produto: {v[2]} | Qtd: {v[3]} | Total: R$ {v[4]:.2f}")
            input("\nPressione Enter para voltar...")
            return
    print("\nVenda não encontrada.")
    input("\nPressione Enter para voltar...")

def menu_vendas():
    carregar_vendas()
    q = -1
    while q != 4:
        limpar_tela()
        print("""
###############################################
######## 1 - NOVA VENDA             ###########
######## 2 - HISTÓRICO DE VENDAS    ###########
######## 3 - BUSCAR VENDA           ###########
######## 4 - VOLTAR                 ###########""")
        try:
            q = int(input("Qual opção você deseja: "))
        except ValueError:
            print("\n[ERRO] Digite apenas números!")
            input("\nPressione Enter para continuar...")
            continue

        if q == 1: nova_venda()
        elif q == 2: historico_vendas()
        elif q == 3: buscar_venda()