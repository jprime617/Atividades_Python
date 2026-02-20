numeros = [237, 518, 604, 392, 844, 327, 967, 124, 731, 856,103, 672, 759, 398, 420, 699, 871, 320, 199, 546,488, 365, 798, 281, 137, 910, 605, 332, 784, 459]
numeros_par = []
numeros_impar = []

for i in numeros:
    if i % 2 == 0:
        numeros_par.append(i)
    else:
        numeros_impar.append(i)

print(f"Numeros Par: {numeros_par} Numeros Impar: {numeros_impar}")
