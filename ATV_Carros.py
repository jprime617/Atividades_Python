carros = ["Gol", "Civic", "Corolla", "Onix", "HB20", "Up"]
carros_minu = []



for i in carros:
    carros_minu.append(i.lower())

print("Carros Disponiveis: ")
for i in enumerate(carros_minu):
    print(i)


while True:
    try:
        qcarro = input("Digite o indice do carro que deseja reservar ou FIM para encerrar: ")
        if int(qcarro) > len(carros_minu) or int(qcarro) < 0:
            print("Deu bosta ai")
        else:    
            break
    except Exception:
        if qcarro.lower() == "fim":
            break
        else:
            print("Deu bosta ai 2")



    
