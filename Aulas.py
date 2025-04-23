# 27/03/2025

def categorias():
    categoria = int(input("Informe a categoria do produto (1 ate 5): "))
    preco = 0


    if categoria == 1:
        preco = 10
    else:
        if categoria == 2:
            preco = 18
        else:
            if categoria == 3:
                preco = 23
            else:
                if categoria == 4:
                    preco = 26
                else:
                    if categoria == 5:
                        preco = 31

    print(f"O valor do produto é: R${preco:.2f}")

def categorias_elif():
    categoria = int(input("Informe a categoria do produto (1 ate 5): "))
    preco = 0

    if categoria == 1:
        preco = 10
    elif categoria == 2:
        preco = 18
    elif categoria == 3:
        preco = 23
    elif categoria == 4:
        preco = 26
    elif categoria == 5:
        preco = 31
    else:
        print("Categoria inválida")
        return

    print(f"O valor do produto é: R${preco:.2f}")

def vendas():
    meta = 20000
    vendas = float(input("Informe o valor das vendas: "))

    if vendas < meta:
        print("Meta não atingida")
    else:
        if vendas > (meta * 2):
            bonus = 0.07 * vendas
        else:
            bonus = 0.03 * vendas
        print(f"Ganhou R${bonus:.2f} de bônus")

# 02/04/2025 lidando com datas e horarios no python

# categorias()
# categorias_elif()
# vendas()

def data_hoje():
    from datetime import datetime
    hoje = datetime.now()
    print(hoje.strftime("A data de hoje é: %d/%m/%Y | %H:%M"))

def data_hoje2():
    from datetime import datetime
    from pytz import timezone

    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone("America/Sao_Paulo")
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime(f"%d/%m/%Y %H:%M")

    print(data_e_hora_sao_paulo_em_texto)

    import pytz

    for tz in pytz.all_timezones:
        print(tz)

    # data_atual = date.today()
    # print("A data atual é: ", data_atual)

    # data_em_texto = data_atual.strftime("A data atual formatada é: %d/%m/%Y")

    # print(data_em_texto)

def revisao():
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))

    if a > b:
        print("O maior numero é", a)
    else:
        print("O maior numero é", b)

def reconstruir():
    ra = input("Entre com o RA de um aluno: ")
    if ra == "155446":
        print("Gabriel Siqueira")
    else:
        if ra == "192804":
            print("Alexsandro Alexandrino")
        else:
            if ra == "209823":
                print("Ana Paula Dantas")
            else:
                if ra == "188948":
                    print("Klairton Brito")
                else:
                    if ra == "999999":
                        print("...")
                    else:
                        print("Aluno não encontrado")

def pograma():
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite outro um numero: "))
    numero3 = int(input("Digite outro um numero: "))

    if (numero1 > numero2) and (numero1 > numero3):
        print(f"{numero1} é o maior")
    elif (numero2 > numero1) and (numero2 > numero3):
        print(f"{numero2} é o maior")
    else:
        print(f"{numero3} é o maior")

# data_hoje()
# data_hoje2()
# revisao()
# pograma()

# 09/04/2025 

def lacos():
    nome = input("digite um nome: ")
    while nome:
        input("insira um nome: ")

    NUM = 1
    while (3 >= NUM):
        print(NUM)
        NUM += 1

def lacos2():
    tabuada = int(input("Digite um numero para tabuada: "))
    n = 1
    while (n <= 10):
        print(n * tabuada)
        n += 1

def lacos3():
    tabuada = 1

    while tabuada <= 10:
        numero = 1
        while numero <= 10:
            print("%d X %d= %d"%(tabuada, numero, tabuada * numero))
            numero += 1
        print("====================")
        tabuada += 1

def lacos4():
    h = 1

    while h <= 12:
        m = 1
        while m <= 59:
            print(f"são {h} horas e {m} minutos")
            m += 1
        h += 1

def lacos5():
    import random

    numero_aleatorio = random.randint(1, 100)
    tentativa = int(input("Adivinhe o numero entre 1 e 100: "))

    while tentativa != numero_aleatorio:
        if tentativa < numero_aleatorio:
            print("muito baixo!")
        else:
            print("muito alto!")
        tentativa = int(input("Tente novamente: "))

    print(f"Parabens vc adivinhou o numero { numero_aleatorio}.")

# lacos()
# lacos2()
# lacos4()
# lacos5()

# 10/04/2025 laços part2 && Listas

def Roi():
    soma_roi = 0

    while True:
        receita = float(input("Qual a sua receita: "))
        custo = float(input("Qual o custo: "))
        ROI = ((receita - custo) / custo) * 100
        soma_roi += ROI

        print(f"Seu ROI é: {ROI:.2f}")

        if input("vc quer Continuar a calcular o Roi? (s/n): ").upper() == "N":
            print(f"A soma dos Roi é: {soma_roi}")
            break
            
def lista():
    lista = [-12,50,25,0,45,9]
    print(type(lista))
    
def lista2():

    cidades = []

    while len(cidades) <= 2:
        cidades.append(input("Digite o nome da cidade: "))
    print(f"{cidades}")

def lista3():
    cidades = []
    estados = []

    tamanho_lista = int(input("Digite o tamanho da lista: "))

    for elemento in range(tamanho_lista):
        cidades.append(input("Digite o nome da cidade: "))
        estados.append(input("Digite o nome do estado: "))
    print(f"As cidades digitadas foram: {cidades}")
    print(f"Os estados digitados foram: {estados}")

def lista4():
    unidade = ["Newton", "Joule", "Kelvin", "Pascal"]
    print(unidade)
    print("No indice =3 temos: ", unidade[-1])
    print("No indice =2 temos: ", unidade[-2])
    print("No indice =1 temos: ", unidade[-3])
    print("No indice =0 temos: ", unidade[-4])

def lista5():
    unidade = ["Newton", "Joule", "Kelvin", "Pascal"]
    print(unidade)
    x = len(unidade)
    for i, elemento in enumerate(unidade):
        print("No indice = ", (x - 1), "temos: ", unidade[x - 1])
        x -= 1

# Roi()
# lista()
# lista2()
# lista3()
# lista4()

# 17/04/2025 

def lista6():
    livros = ["Java", "SqlServer", "Delphi", "Python"]
    livros.append("Android")
    livros.insert(0, "Oracle")
    print(livros)
    livros.pop(5)
    print(livros)
    livros.remove("Delphi")
    print(livros)
    livros.sort()
    print(livros)
    livros.reverse()
    print(livros)

def lista7():
    lista = []
    for x in range(5):
        n = int(input("Digite um numero: "))
        lista.append(n)
        lista.sort()
    print(lista)

# lista6()
# lista7()

# 23/04/2025 

# def algoritmo():
#     lista = [15,7,27,39]

#     achou = False
#     rep = True

#     while rep:
#         procurado = int(input("Digite o numero a ser procurado: "))

#         for i in range(len(lista)):
#             if lista[i] == procurado:
#                 achou = True

#             if achou:
#                 print(f"O numero {procurado} foi encontrado na posição {i + 1}")
#                 i = 0
#                 break
#             else:
#                 print(f"O numero {procurado} não foi encontrado")
#                 i = 0
#                 break
        
#         achou = False
        
#         res = input("Quer continuar? (s/n): ").lower()
#         if res == "n":
#             rep = False

def algoritmo2():
    lista = [15,7,27,39]
    procurado = int(input("Digite o numero a ser procurado: "))

    achou = False
    x = 0

    while x < len(lista):
        if lista[x] == procurado:
            achou = True
            break
        x += 1
    if achou:
        print(f"O numero {procurado} foi encontrado na posição {x + 1}")
    else:
        print(f"O numero {procurado} não foi encontrado")

def lista8():
    lista = [1,7,2,4,0]
    maximo = lista[0]
    minimo = lista[0]

    for i in lista:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
    print(f"maximo: {maximo}, minimo: {minimo}")

def lista9():
    valores = [9,8,7,12,0,13,21]
    pares = []
    impares = []

    for i in valores:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

def lista10():
    lista = [1, 4,5,6,4,7]

    valor = 4
    remove = False
    temp = []

    for i in range(len(lista)):
        if lista[i] != valor or remove:
            temp.append(lista[i])
        else:
            remove = True

    lista = temp

    print(lista)

# algoritmo() # BRUH
# algoritmo2()
# lista8()
# lista9()
# lista10()

