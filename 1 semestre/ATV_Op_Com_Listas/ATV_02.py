Nomes = ["Ana","Bruno","Carla","Daniel","Eduarda","Felipe","Gabriela","Henrique","Isabela","João","Karina","Lucas","Mariana","Nicolas","Olívia"]
Nomes_Minus = []

# for i in range(15):
#     Nomes.append(str(input("Adicione um nome a lista de nomes: ")))

for i in Nomes:
    Nomes_Minus.append(i.lower())

print(Nomes_Minus)

nome = str(input("Digite o nome que quer procurar: ")).lower()

for x in range(len(Nomes_Minus)):
    if nome == Nomes_Minus[x]:
        print(f"{Nomes_Minus[x]} Encontrado no indice {x}")
        break
else:
        print(f"Nome não encontrado no indice {0 -1}")
