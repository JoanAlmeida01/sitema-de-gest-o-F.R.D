import os

clientes = []
ARQUIVO_CLIENTES = "clientes.txt"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = "".join(char for char in cpf if char.isdigit())

    # Verifica se tem 11 dígitos ou se são todos números iguais (ex: 111.111.111-11)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito_1 = 0 if resto == 10 else resto

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito_2 = 0 if resto == 10 else resto

    return cpf[9] == str(digito_1) and cpf[10] == str(digito_2)

def salvar_clientes():
    try:
        with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as arquivo:
            for cliente in clientes:
                # Salvando o CPF como string limpa ou formatada
                arquivo.write(f"{cliente[0]};{cliente[1]};{cliente[2]};{cliente[3]}\n")
    except Exception as e:
        print(f"Erro ao salvar clientes: {e}")

def carregar_clientes():
    global clientes
    clientes.clear()
    if os.path.exists(ARQUIVO_CLIENTES):
        try:
            with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if linha:
                        dados = linha.split(";")
                        if len(dados) == 4:
                            # Mantemos dados[0] (CPF) como string
                            clientes.append([dados[0], dados[1], dados[2], dados[3]])
        except Exception as e:
            print(f"Erro ao carregar clientes: {e}")

# --- FUNÇÃO DE ACOPLAMENTO PARA O MAIN.PY ---
def carregar_dados():
    """Função padrão chamada pelo main.py para garantir a leitura do arquivo txt"""
    carregar_clientes()

def cadastrar_cliente():
    limpar_tela()
    print("### CADASTRAR CLIENTE ###\n")
    
    cpf = input("Digite o CPF (apenas números ou formatado): ").strip()
    cpf_limpo = "".join(char for char in cpf if char.isdigit())
    
    if not validar_cpf(cpf_limpo):
        print("\n[ERRO] CPF inválido!")
        input("\nPressione Enter para voltar...")
        return

    if any(c[0] == cpf_limpo for c in clientes):
        print("\n[ERRO] Já existe um cliente com este CPF!")
        input("\nPressione Enter para voltar...")
        return

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")

    clientes.append([cpf_limpo, nome, telefone, cidade])
    salvar_clientes()
    print("\nCliente cadastrado com sucesso!")
    input("\nPressione Enter para voltar...")

def listar_clientes():
    limpar_tela()
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        print("=" * 80)
        print(f"{'LISTANDO TODOS OS CLIENTES':^80}")
        print("=" * 80)
        print(f"{'CPF':<15} | {'NOME':<25} | {'TELEFONE':<15} | {'CIDADE':<15}")
        print("-" * 80)
        for c in clientes:
            # Formata o CPF para exibição bonita (###.###.###-##)
            cpf_formatado = f"{c[0][:3]}.{c[0][3:6]}.{c[0][6:9]}-{c[0][9:]}"
            print(f"{cpf_formatado:<15} | {c[1]:<25} | {c[2]:<15} | {c[3]:<15}")
        print("=" * 80)
    input("\nPressione Enter para voltar...")

def buscar_cliente():
    limpar_tela()
    cpf = input("Digite o CPF do cliente para buscar: ").strip()
    cpf_limpo = "".join(char for char in cpf if char.isdigit())
    
    for c in clientes:
        if c[0] == cpf_limpo:
            cpf_formatado = f"{c[0][:3]}.{c[0][3:6]}.{c[0][6:9]}-{c[0][9:]}"
            print(f"""
            CPF: {cpf_formatado}
            Nome: {c[1]}
            Telefone: {c[2]}
            Cidade: {c[3]}""")
            input("\nPressione Enter para voltar...")
            return
    print("\nCliente não encontrado.")
    input("\nPressione Enter para voltar...")

def atualizar_cliente():
    limpar_tela()
    cpf = input("Digite o CPF do cliente que deseja atualizar: ").strip()
    cpf_limpo = "".join(char for char in cpf if char.isdigit())
    
    for c in clientes:
        if c[0] == cpf_limpo:
            c[1] = input("Novo nome: ")
            c[2] = input("Novo telefone: ")
            c[3] = input("Nova cidade: ")
            salvar_clientes()
            print("\nCliente updated!")
            input("\nPressione Enter para voltar...")
            return
    print("\nCliente não encontrado.")
    input("\nPressione Enter para voltar...")

def remover_cliente():
    limpar_tela()
    cpf = input("Digite o CPF do cliente que deseja remover: ").strip()
    cpf_limpo = "".join(char for char in cpf if char.isdigit())
    
    for c in clientes:
        if c[0] == cpf_limpo:
            confirmar = input("Tem certeza que deseja remover? [S/N]: ").upper()
            if confirmar == "S":
                clientes.remove(c)
                salvar_clientes()
                print("\nCliente removido com sucesso!")
            input("\nPressione Enter para voltar...")
            return
    print("\nCliente não encontrado.")
    input("\nPressione Enter para voltar...")

def menu_clientes():
    carregar_clientes()
    q = -1
    while q != 6:
        limpar_tela()
        print("""
###############################################
######## 1 - CADASTRAR CLIENTE       ##########
######## 2 - LISTAR CLIENTES         ##########
######## 3 - BUSCAR CLIENTE          ##########
######## 4 - ATUALIZAR CLIENTE       ##########
######## 5 - REMOVER CLIENTE         ##########
######## 6 - VOLTAR                  ##########""")
        try:
            q = int(input("Qual opção você deseja: "))
        except ValueError:
            print("\n[ERRO] Digite apenas números!")
            input("\nPressione Enter para continuar...")
            continue

        if q == 1: cadastrar_cliente()
        elif q == 2: listar_clientes()
        elif q == 3: buscar_cliente()
        elif q == 4: atualizar_cliente()
        elif q == 5: remover_cliente()

# Para testar diretamente o menu se rodar este arquivo
if __name__ == "__main__":
    menu_clientes()