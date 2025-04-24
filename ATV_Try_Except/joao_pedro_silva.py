


def filtro_STR(entrada):
    try:
        if int(entrada) / 1: 
            
            return -1
    except:
        return entrada
    
def filtro_INT(entrada):
    try:
        if int(entrada) / 1:
            return int(entrada)
    except:
        return "N_inteiro"


def atv01():
    lista = []

    
    while True:
        tarefa = filtro_STR(input("Digite uma tarefa ou FIM para encerrar: "))
        if str(tarefa).lower() == "fim":
            lista.sort()
            print(lista)
            break
        else:
            if tarefa == -1:
                print("Digite um texto!!! \n")
            else:
                for i in lista:
                    if tarefa.lower() == i:
                        print("Essa Tarefa ja existe na lista!!!")
                        break
                else:
                    lista.append(tarefa.lower())
                    print("Tarefa Adicionada")

def atv02():
    estoque = []

    while True:
        escolha = str(input("Voce deseja ADICIONAR , REMOVER ou CONTAR produtos? (digite): ")).lower()

        if escolha == "adicionar":
            produto_a = filtro_STR(input("Digite o produto para adicionar: "))
            if produto_a == -1:
                print("Digite um texto")
            else:
                estoque.append(produto_a)
                print(estoque)


        if escolha == "remover":
            produto_r = filtro_STR(input("Digite o produto para remover: "))
            if produto_r == -1:
                print("Digite um texto")
            else:
                try:
                    estoque.remove(produto_r)
                    print(estoque)
                except ValueError:
                    print("Esse produto não existe na lista!!!")


        if escolha == "contar":
            produto_c = filtro_STR(input("Digite um produto para contar: "))
            if produto_c == -1:
                print("Digite um texto")
            else:
                try:
                    print(estoque.count(produto_c.lower()))

                except ValueError:
                    print("Esse produto nao existe na lista!!!")

def atv03():
    num = filtro_INT(input("Digite um numero que sera convertido para inteiro: "))
    if num == "N_inteiro":
        print("Não pode ser convertido pois é um texto!!!")
    else:
        num_int = int(num)
        print(f"Convertido para inteiro {num_int}")

def atv04():
    lista = ["banana", "sabonete", "chocolate"]

    while True:
        print(lista)
        escolha = filtro_STR(input("Voce Deseja remover usando NOME ou INDICE? "))

        try:

            if escolha.lower() == "nome":
                entrada1 = filtro_STR(input("Digite o nome do produto: "))
                if entrada1 == -1:
                    print("Digite um Texto!!!")
                else:
                    try:
                        lista.remove(entrada1)
                    except:
                        print("Nome nao encontrado")


            if escolha.lower() == "indice":
                entrada2 = filtro_INT(input("Digite o indice do produto: "))
                if entrada2 == "N_inteiro":
                    print("Escreva um numero")
                else:
                    try:
                        lista.pop(entrada2)
                    except:
                        print("Esse indice nao existe")


            if escolha.lower() != "nome" and escolha.lower() != "indice":
                print("Voce escreveu errado")
        except:
            print("voce escreveu errado")
            




# atv01()
# atv02()
# atv03()
# atv04()