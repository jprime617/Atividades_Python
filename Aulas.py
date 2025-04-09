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
pograma()
