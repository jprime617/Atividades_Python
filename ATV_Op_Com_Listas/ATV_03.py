Nomes = ["Ana","Bruno","Carla","Daniel","Eduarda","Felipe","Gabriela","Henrique","Isabela","João","Karina","Lucas","Mariana","Nicolas","Olívia"]
Nomes_Minus = []

# for i in range(15):
#     Nomes.append(str(input("Adicione um nome a lista de nomes: ")))

for i in Nomes:
    Nomes_Minus.append(i.lower())

print(Nomes_Minus)

nome = str(input("Digite o nome que quer procurar: ")).lower()
x = 0

while x < len(Nomes_Minus):
    if nome == Nomes_Minus[x]:
        print(f"{nome} Encontrado no indice {x}")
        break

    x += 1

else:
    print(f"Nome não encontrado {0 -1}, interaçoes: {x}")

