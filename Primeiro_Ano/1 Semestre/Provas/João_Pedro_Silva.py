
# Difinindo Variaveis.


Lista_Nomes = []            # Lista dos nomes.
select_Menu = 0             # Forma de selecionar uma Opção no Menu.
select_Cadastro = ""        # Forma de selecionar uma Opção no Cadastro de Nomes.
cadastro_cancelado = 0      # Variavel para guardar a quantidade de vezes que o cadastro foi cancelado.


# While para fazer a seleção do Menu, caso a resposta seja diferente de 0 ou 1 responda novamente, se for 0: Fim do Programa
while True:
    try:
        select_Menu = int(input("\nSelecione:\n\n- 1 - Iniciar Cadastro \n- 0 - Sair do Sistema\n\n: "))

        if select_Menu == 0 or select_Menu == 1:
            break
        else:
            print("\nDigite uma das Opções!")
    except ValueError:
        print("\nDigite uma das Opções!")



# While para fazer os cadastros de Nomes, se a resposta for Vazia: Digite Novamente, se for Sair: Fim do programa
# Select_Menu == 1, a resposta do While anterior deve ser 1, caso nao seja ir direto para o fim.
while select_Menu == 1:
    
    try:
        select_Cadastro = str(input("Digite o nome do aluno ou 'sair' para encerrar o cadastro: ")).lower()
        if select_Cadastro == "" or not select_Cadastro.isalpha():
            print("\nDigite Novamente!\n")
        else:
            if select_Cadastro == "sair":
                print("\nSaiu\n")
                break
            else:
                # Caso a resposta de select_cadastro seja valida checar se existe esse nome na lista, se sim voltar para select_cadastro.
                if select_Cadastro in Lista_Nomes:
                    print("\nNome ja cadastrado!\n")

                else:
                    # Caso o nome nao seja encontrado na lista entao vamos adicionar ele, se a resposta for Nao ou Nulo Cancelar Cadastro.
                    check_Cadastro = str(input(f"\nDeseja Cadastrar {select_Cadastro}? (sim/não): ")).lower()
                    if check_Cadastro == "":
                        print("\nResposta invalida \nCadastro Cancelado!\n")
                        cadastro_cancelado += 1
                    else:
                        if check_Cadastro == "não" or check_Cadastro == "nao":
                            print("\nCadastro Cancelado!\n")
                            cadastro_cancelado += 1
                        else:
                            # Se o check_Cadastro igual a sim entao cadastra o nome na lista
                            if check_Cadastro == "sim":
                                Lista_Nomes.append(select_Cadastro)
                                print("\nCadastro Realizado com Sucesso!\n")
                            else:
                                print("\nResposta Invalida! \nCadastro Cancelado\n")
                                cadastro_cancelado += 1
    except:
        print("\n\nDigite Novamente! Except\n")

# Se a lista existe e o select_Menu diferente de 0 no caso 1, ja que nao é possivel ser qualquer outro numero ou letra, mostrar a lista e as informações adicionais
if Lista_Nomes and select_Menu != 0:
    print("\nLista: \n")
    print("##############################################")
    for i in range(len(Lista_Nomes)):
        print(f"-{i + 1}- {Lista_Nomes[i]}")
    print("##############################################")

    print(f"\nVocê Cadastrou {len(Lista_Nomes)} Nomes!")
    print(f"\nVocê Cancelou {cadastro_cancelado} Vezes o Cadastro!\n")

                    
                    
# Fim do Programa
print("FIM")




