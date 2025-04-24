produtos = ["Arroz","Feijão","Macarrão","Óleo","Leite","Pão","Café","Açúcar","Farinha","Molho de tomate"]
produtos_minus = []
precos = [5.49,6.99,3.89,4.79,4.99,2.50,8.25,3.15,4.60,2.99]

for i in produtos:
    produtos_minus.append(i.lower())

print(produtos_minus)

nome_pro = str(input("Digite o nome do produto: ")).lower()

# for produto in enumerate(produtos):
#     print(produto)

for x in range(len(produtos_minus)):
    if nome_pro == produtos_minus[x]:
        print(f"{nome_pro} : R${precos[x]:.2f}")
else:
    print(f"Produto não encontrado")