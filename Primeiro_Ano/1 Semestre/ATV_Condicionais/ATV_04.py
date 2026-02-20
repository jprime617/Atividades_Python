peso = float(input("Qual o seu peso: "))
altura = float(input("Qual a sua altura: "))
imc_resposta = ""
imc = peso / (altura ** 2)

if imc < 18.5:
    imc_resposta = "Abaixo do peso"
else:
    if imc >= 18.5 and imc <= 24.9:
        imc_resposta = "Peso normal"
    else:
        if imc >= 25 and imc <= 29.9:
            imc_resposta = "Sobrepeso"
        else:
            imc_resposta = "Obesidade"

print(f"Seu IMC é: {imc_resposta}")