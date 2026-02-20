lista = []

for x in range(10):
    lista.append(int(input(f"Digite um numero para colocar na lista ({len(lista)} / 10): ")))

valor = int(input("Digite o valor repetido que quer remover: "))
remove = False
temp = []

for i in range(len(lista)):
    if lista[i] != valor or remove:
        temp.append(lista[i])
    else:
        remove = True

lista = temp

print(lista)