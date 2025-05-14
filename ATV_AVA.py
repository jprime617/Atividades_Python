vendas = [
 ('05/09/2020', 'iPhone 13', 'preto', '256GB', 12, 6000),
 ('05/09/2020', 'iPhone 13', 'azul', '256GB', 8, 6000),
 ('05/09/2020', 'Samsung Galaxy S21', 'preto', '128GB', 15, 4000),
 ('05/09/2020', 'Xiaomi 12', 'preto', '256GB', 20, 3000),
 ('05/09/2020', 'Xiaomi 12', 'azul', '256GB', 10, 3000),
 ('05/09/2020', 'Motorola Edge', 'preto', '128GB', 9, 2800),
 ('05/09/2020', 'LG Wing', 'rosa', '128GB', 7, 2500),
 ('05/09/2020', 'Nokia 6.2', 'preto', '64GB', 11, 1600),
 ('05/09/2020', 'iPhone 11', 'verde', '128GB', 10, 4000),
 ('05/09/2020', 'iPhone SE', 'vermelho', '64GB', 6, 3200),
]

faturamento = 0

for item in vendas:
    data, nome, cor, gb, quant_vendidos, preco = item
    if cor.lower() == "preto":
        faturamento1 += quant_vendidos * preco


print(f"O Faturamento dos produtos com cor preta foi de: R$:{faturamento1:,.2f}")