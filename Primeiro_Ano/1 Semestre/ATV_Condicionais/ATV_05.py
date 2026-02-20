km = float(input("Quantos km o onibus andou: "))
custo_passagem = 0

if km <= 200:
    custo_passagem = km * 0.50
else:
    custo_passagem = km * 0.45

print(f"O custo da passagem foi R${custo_passagem:.2f}")