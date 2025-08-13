salario_atual = float(input("Qual o seu salario atual: "))
salario_novo = 0

if salario_atual < 2000:
    salario_novo = salario_atual * 1.15
else:
    salario_novo = salario_atual * 1.10

print(f"Seu novo salario é R${salario_novo:.2f}")