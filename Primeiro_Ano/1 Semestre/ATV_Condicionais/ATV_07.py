valor_compra = float(input("Qual foi o valor total da compra: "))
desconto = 0

if valor_compra > 500:
    # valor_novo = valor_compra - (valor_compra * 0.10)
    desconto = 0.10
else:
    if valor_compra >= 200 and valor_compra <= 500:
        # valor_novo = valor_compra - (valor_compra * 0.05)
        desconto = 0.05


print(f"O Valor da compra ficou: R${valor_compra - (valor_compra * desconto):.2f}")