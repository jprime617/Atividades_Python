Nomes = []

for i in range(15):
    Nomes.append(str(input("Adicione um nome a lista de nomes: ")))

nome = str(input("Digite o nome que quer procurar: "))

for x in range(len(Nomes)):
    if nome == Nomes[x]:
        print(f"{Nomes[x]} Esse aqui existe e vc achou em {x + 1} voltas")

