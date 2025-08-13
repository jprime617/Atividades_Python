tenho_fome = input("Esta com fome? (s/n): ")

if tenho_fome.lower() == "s":
    tem_comida = input("voce tem comida em casa? (s/n): ")
    if tem_comida.lower() == "n":
        print("Ir ao mercado")
        print("Voltar para casa")
    print("Preparando comida")
    print("Comer comida")
print("Fim")

