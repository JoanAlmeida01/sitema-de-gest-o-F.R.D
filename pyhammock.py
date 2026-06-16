resp = -1
estoque = []
clientes = []
vendas = []

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
######## 0 - SAIR                    ##########
""")

    resp = int(input("Qual opção você deseja: "))


    if resp == 1:

        q = -1

        while q != 6:

            print("""
###############################################
#         GERENCIAMENTO DE ESTOQUE            #
###############################################
######## 1 - CADASTRAR REDE          ##########
######## 2 - LISTAR REDES            ##########
######## 3 - ATUALIZAR REDE          ##########
######## 4 - BUSCAR REDE             ##########
######## 5 - REMOVER REDE            ##########
######## 6 - VOLTAR                  ##########
""")

            q = int(input("Qual opção você deseja: "))

            if q == 1:

               codigo = int(input("Digite o código da rede: "))
               modelo = input("Digite o modelo da rede: ")
               cor = input("Digite a cor da rede: ")
               material = input("Digite o material da rede: ")
               preco = float(input("Digite o preço da rede: "))
               quantidade = int(input("Digite a quantidade em estoque: "))

               estoque.append([
                 codigo,
                 modelo,
                 cor,
                 material,
                 preco,
                 quantidade
               ])

               print("Rede cadastrada com sucesso!")

            elif q == 2:

               if len(estoque) == 0:
                  print("Nenhuma rede cadastrada.")

               else:
                  print("\nLISTANDO TODAS AS REDES...\n")

                  for item in estoque:

                    print(f"""
            CÓDIGO: {item[0]}
            MODELO: {item[1]}
            COR: {item[2]}
            MATERIAL: {item[3]}
            PREÇO: R$ {item[4]:.2f}
            QUANTIDADE: {item[5]}
            --------------------------------
            """)

            elif q == 3:
                print("ATUALIZAR REDE")

            elif q == 4:

               codigo = int(input("Digite o código da rede: "))

               encontrado = False

               for item in estoque:

                if item[0] == codigo:

                   print(f"""
           ### REDE ENCONTRADA ###

           CÓDIGO: {item[0]}
           MODELO: {item[1]}
           COR: {item[2]}
           MATERIAL: {item[3]}
           PREÇO: R$ {item[4]:.2f}
           QUANTIDADE: {item[5]}
           """)

                   encontrado = True

                if not encontrado:
                   print("Rede não encontrada.")

            elif q == 5:

              codigo = int(input("Digite o código da rede que deseja remover: "))
              encontrado = False
              for item in estoque:

                if item[0] == codigo:

                    confirmar = input(
                        "Tem certeza que deseja remover? [S/N]: "
                    ).upper()

                    if confirmar == "S":
                        estoque.remove(item)
                        print("Rede removida com sucesso!")

                    encontrado = True
                    break

            if not encontrado:
             print("Rede não encontrada.")

    elif resp == 2:

        q = -1

        while q != 6:

            print("""
###############################################
######## 1 - CADASTRAR CLIENTE       ##########
######## 2 - LISTAR CLIENTES         ##########
######## 3 - BUSCAR CLIENTE          ##########
######## 4 - ATUALIZAR CLIENTE       ##########
######## 5 - REMOVER CLIENTE         ##########
######## 6 - VOLTAR                  ##########
""")

            q = int(input("Qual opção você deseja: "))

            if q == 1:
               codigo = int(input("Código: "))
               nome = input("Nome: ")
               telefone = input("Telefone: ")
               cidade = input("Cidade: ")
               clientes.append([codigo, nome, telefone, cidade])
               print("Cliente cadastrado!")

            elif q == 2:

              if len(clientes) == 0:
               print("Nenhum cliente cadastrado.")

              else:
                for c in clientes:
                 print(f"""
            Código: {c[0]}
            Nome: {c[1]}
            Telefone: {c[2]}
            Cidade: {c[3]}
            -------------------------
            """)
                 
            elif q == 3:

              codigo = int(input("Digite o código: "))
              encontrado = False

              for c in clientes:
                  if c[0] == codigo:
                      print(c)
                      encontrado = True

              if not encontrado:
                  print("Cliente não encontrado.")

            elif q == 4:

                 codigo = int(input("Código do cliente: "))

                 for c in clientes:

                     if c[0] == codigo:

                         c[1] = input("Novo nome: ")
                         c[2] = input("Novo telefone: ")
                         c[3] = input("Nova cidade: ")

                         print("Cliente atualizado!")
                         break

            elif q == 5:

              codigo = int(input("Digite o código da rede que deseja remover: "))

              encontrado = False

              for item in estoque:

                if item[0] == codigo:

                    confirmar = input(
                        "Tem certeza que deseja remover? [S/N]: "
                    ).upper()

                    if confirmar == "S":
                        estoque.remove(item)
                        print("Rede removida com sucesso!")

                    encontrado = True
                    break

            if not encontrado:
             print("Rede não encontrada.") 

    elif resp == 3:

        q = -1

        while q != 4:

            print("""
###############################################
######## 1 - NOVA VENDA             ###########
######## 2 - HISTÓRICO DE VENDAS    ###########
######## 3 - BUSCAR VENDA           ###########
######## 4 - VOLTAR                 ###########
""")

            q = int(input("Qual opção você deseja: "))

            if q == 1:

                cod_venda = int(input("Código da venda: "))
                cod_cliente = int(input("Código do cliente: "))
                cod_produto = int(input("Código da rede: "))
                qtd = int(input("Quantidade: "))

                for item in estoque:

                    if item[0] == cod_produto:

                        if item[5] >= qtd:

                            total = qtd * item[4]

                            item[5] -= qtd

                            vendas.append([
                                cod_venda,
                                cod_cliente,
                                cod_produto,
                                qtd,
                                total
                            ])

                            print("Venda realizada!")
                            print(f"Total: R$ {total:.2f}")

                        else:
                            print("Estoque insuficiente.")

                        break

            elif q == 2:

                for v in vendas:

                    print(f"""
            Venda: {v[0]}
            Cliente: {v[1]}
            Produto: {v[2]}
            Quantidade: {v[3]}
            total: R$ {v[4]:.2f}
            ------------------------
            """)

            elif q == 3:

                codigo = int(input("Código da venda: "))

                for v in vendas:

                    if v[0] == codigo:
                        print(v)
                        break

    
    elif q == 4:

        print("Quantidade de vendas:", len(vendas))

        q = -1

        while q != 5:

            print("""
###################################################
############ 1 - TOTAL FATURADO            ########
############ 2 - REDE MAIS VENDIDA         ########
############ 3 - CLIENTES QUE MAIS COMPRAM ########
############ 4 - QUANTIDADE DE VENDAS      ########
############ 5 - VOLTAR                    ########
""")

            q = int(input("Qual opção você deseja: "))

            if q == 1:
                print("TOTAL FATURADO")

            elif q == 2:
                print("REDE MAIS VENDIDA")

            elif q == 3:
                print("CLIENTES QUE MAIS COMPRAM")

            elif q == 4:
                print("QUANTIDADE DE VENDAS")


    elif resp == 5:

        print("""
###################################################
##########      MÓDULO INFORMAÇÕES       ##########
###################################################

### PROJETO DE PROGRAMAÇÃO EM PYTHON            ###
### TEMA: SISTEMA DE REDES DE DORMIR            ###
### DISCENTE: SEU NOME                          ###
### UTILIZAÇÃO DE MATRIZES E LISTAS             ###
""")


    elif resp == 0:

        print("""
#################################
##### PROGRAMA ENCERRADO #####
#################################
""")

    else:
        print("OPÇÃO INVÁLIDA!")