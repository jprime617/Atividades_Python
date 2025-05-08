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

# 24/04/2025 Try except

# def tex1():
#     x = 12
#     y = 0
#     try:
#         z = x/y
#     except ZeroDivisionError:
#         print("Erro: Dividsite por zero, meu kiridu!!!!!")

# def ler_int(mensagem, mensagem_erro):
#     while True:
#         try:
#             entrada = int(input(mensagem))
#             return entrada
#         except ValueError:
#             print(mensagem_erro)

# def div():
#     print("Vamos dividir dois numeros inseridos por voce\n")
#     num1 = input("Insira o primeiro numero: ")
#     num2 = input("Insira o segundo numero: ")
#     try:
#         resultado = int(num1) / int(num2)
#         print("O resultado é " + str(resultado))
#     except ZeroDivisionError:
#         print("Deu erro Zero Div")
#     except ValueError:
#         print("Deu erro Value Error")
#     except Exception:
#         print("Deu Erro GERAL")

# def tex2():
#     try:
#         idade = int(input("Digite sua idade: "))
#         if idade <= 0 or idade >= 110:
#             raise ValueError("A idade deve ser um numero positivo.")
#     except ValueError as erro:
#         raise ValueError(f"Erro de entrada: {erro}")


# tex1()
# MSG = "Digite um numero inteiro: "
# MSG_ERRO = "Numero invalido!!!"
# x = ler_int(MSG, MSG_ERRO)
# y = ler_int(MSG, MSG_ERRO)
# print(x+y)
# div()
# tex2()


# 30/04/2025 funções def

# def soma(a,b):
#     print(a + b)

# soma(2,9)
# soma(45,45)

# valor_A = int(input("Digite um valor A: "))
# valor_B = int(input("Digite um valor B: "))

# soma(valor_A, valor_B)

# import random

# def criaListaAleatoria(tamanho) :
#     lista = []
#     for i in range(tamanho):
#         valor = random.randint(1,10)
#         lista.append(valor)
#     return lista, max(lista), min(lista)

# tam = 5

# li, maxli, minli = criaListaAleatoria(tam)

# print(li)
# print(maxli)
# print(minli)


# def somar(a,b,c):
#     soma = a + b + c
#     return soma

# num1 = int(input("Digite o numero 1: "))
# num2 = int(input("Digite o numero 2: "))
# num3 = int(input("Digite o numero 3: "))

# print(f"A Soma dos numeros é: {somar(num1,num2,num3)}")



# funcoes part 2

# lista = ["Retangulo", "Triagulo", "Circulo"]
# lista_Funcoes = [area_Retangulo(), area_Triangulo()]


# def area_Retangulo(lado_a,lado_b):
#     area = lado_a * lado_b
#     return area

# def area_Triangulo(base, altura):
#     area = (base * altura) / 2
#     return area

# def area_Circulo(raio):
#     area = 3.14 * (raio ** 2)
#     return area


# def Menu(items_Menu, questao):

#     contador = 1
#     print(questao)
#     for i in items_Menu:
#         print(f"{contador} - {i}")
#         contador += 1
#     print("0 - Fim")

#     for i in range(len(items_Menu)):

#         print(i)

#         match selection:
#             case i:



#     selection = int(input("Digite: "))

#     if selection == 1:
#         print(area_Retangulo(int(input("Digite a base: ")), int(input("Digite a altura: "))))
#     elif selection == 2:
#         print(area_Triangulo(int(input("Digite a base: ")), int(input("Digite a altura: "))))
#     elif selection == 3:
#         print(area_Circulo(int(input("Digite o raio: "))))
#     elif selection == 0:
#         print("FIM")
#         return

# Menu(lista, "Escolha o objeto que deseja calcular a area:")


# 07/05/2025

lista_alunos = []
lista_notas = []

def alunos():

    while True:
        aluno = str(input("Digite o nome do aluno ou FIM para sair: "))
        if aluno.lower() == "fim":
            break
        else:
            if aluno == "":
                print("Digite algo na caixa bobao!")
            else:
                nota = float(input("Digite a nota do aluno: "))
                lista_alunos.append(aluno.lower())
                lista_notas.append(nota)

    if lista_alunos:

        media = sum(lista_notas) / len(lista_alunos)
        print(media)


        for i in range(len(lista_alunos)):  
            if lista_notas[i] > media:
                print(f"Aluno {lista_alunos[i]} foi acima da media")
    else:
        return
        
# alunos()

def alunos_prof():
    Alunos_Idade = []

    for i in range(5):
        linha = []
        linha.append(input("Digite o nome do aluno " + str(i) + ":"))
        print(linha)
        linha.append(int(input("Digite a idade do aluno " + linha[0] + ":")))
        print(linha)
        Alunos_Idade.append(linha)

# alunos_prof()

a = (3, "maio", 9.5, 1)
print(a[1:3])
