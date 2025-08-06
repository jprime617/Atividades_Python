import random

notas = []
nota = 0

#  INPUT
# while nota != -1:
#     nota = float(input("Digite uma nota ai e -1 para sair: "))
#     if nota != -1.0:
#         notas.append(nota)

#  RANDOM
while nota != -1:
    if len(notas) >= 20:
        nota = -1
    else:
        notas.append(round(random.uniform(0,10),1))

# for i in notas:
#     if i > 7.0:
#         print(i)


# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# print(matriz[1][2])



print(notas)



minn = 0
maxn = 0
total = 0
for i in notas:
    if i > minn:
        minn = i
    if i < maxn:
        maxn = i
    total += i

media = sum(notas) / len(notas)


print(f"A media das notas é: {media:.2f}") # total ou sum(notas)
print(f"A Maior nota é: {maxn}") # ou max(notas)
print(f"A Menor nota é: {minn}") # ou min(notas)


# print(round(random.uniform(0,10),0))