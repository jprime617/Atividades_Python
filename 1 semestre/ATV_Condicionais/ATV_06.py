numero = int(input("Digite um numero: "))
par_impar = ""

if numero % 2 == 0:
    par_impar = "par"
else:
    par_impar = "impar"

print(f"O numero é {par_impar}")