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




# categorias()
# categorias_elif()
vendas()

