from colorama import Fore, Back, Style

carros = ["Gol", "Civic", "Corolla", "Onix", "HB20", "Up"]
carros_reservados = []



for i in carros:
    indi = carros.index(i)
    carros[indi] = i.lower()

print(carros)

print(Fore.YELLOW + "Carros Disponiveis: ")
print(Style.RESET_ALL)

for i in enumerate(carros):
    print(i)

def reserva():
    carros_reservados.append(carros[int(qcarro)])
    print(Fore.GREEN + f"{carros[int(qcarro)]} Reservado!")
    return


while True:
    try:
        qcarro = input(Fore.YELLOW + "Digite o indice do carro que deseja reservar ou FIM para encerrar: ")
        
        if int(qcarro) > len(carros) -1 or int(qcarro) < 0:
            print(Fore.RED + "Numero Invalido")
        else:    
            reserva()
    except Exception as e:
        if qcarro.lower() == "fim":
            print(Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Digite um Numero")

if carros_reservados:
    print(f"Carros Reservados: {carros_reservados}")
    print(Fore.GREEN + "Obrigado Pela Reserva")
    print(Style.RESET_ALL)





    
