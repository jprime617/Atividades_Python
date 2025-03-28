velocidade = float(input("Qual a velocidade do veiculo (km/h): "))
limite = 80
multa = 0
resposta = ""

if velocidade > limite:
    multa = 5
    resposta = f"A sua multa foi de R${(velocidade - limite) * multa:.2f}"
else:
    resposta = f"Voce esta dentro do limite de velocidade"

print(resposta)
