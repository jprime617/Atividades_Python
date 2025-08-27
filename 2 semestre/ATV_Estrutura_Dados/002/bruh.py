import random

Gundam_lista = [
    "Wing Gundam (Bird Mode)",
    "Gundam Heavyarms",
    "Gundam Sandrock",
    "Maganac",
    "Leo",
    "Aries",
    "Tragos",
    "RX-78-2 Gundam",
    "RX-78-2 Gundam (MA Form)",
    "Guncannon",
    "Guntank",
    "GM RGM-79",
    "Gundam Aerial (Permet Score Six)",
    "Gundam Aerial (Bit on Form)",
    "Demi Trainer MSJ-121",
    "Zowort F/O-19",
    "Aile Strike Gundam",
    "Strike Gundam",
    "Moebius Zero",
    "Moebius",
    "Strike Dagger",
    "Aegis Gundam (MA Mode)",
    "Ginn",
    "Miguel’s Ginn",
]

class Carta:
    def __init__(self, name):
        self.Name = name
        self.Atk = random.randint(1,6)
        self.Def = random.randint(3,12)
        self.Spd = random.randint(1,10)
        
Pilha = []
Pilha2 = []

for i in Gundam_lista:
    Pilha.append(Carta(i))
    Pilha2.append(Carta(i + " Enemy"))

Fila = []
Fila2 = []

def Ordenar(X):
    for i in X:
        n = 0
        if i.Spd > n:
            carta = X.pop(i)
            X.append(carta)
        n = i


def Adicionar():
    while len(Fila) < 5 and Pilha:
        Fila.append(Pilha.pop(-1))
        

    while len(Fila2) < 5 and Pilha2:
        Fila2.append(Pilha2.pop(-1))
        
    
    # Fila.sort(key=lambda x: x.Spd, reverse=True)
    # Fila2.sort(key=lambda x: x.Spd, reverse=True)
    Ordenar(Fila)

    for i in Fila:
        print(i.Spd)



def Batalha():
    while Fila and Fila2:  # enquanto houver cartas nas filas
        carta1 = Fila.pop(0)
        carta2 = Fila2.pop(0)

        Adicionar()

        print("\n=== Novo Duelo ===")
        print(f"JOGADOR: {carta1.Name} | ATK:{carta1.Atk} DEF:{carta1.Def} SPD:{carta1.Spd}")
        print(f"ENEMY:   {carta2.Name} | ATK:{carta2.Atk} DEF:{carta2.Def} SPD:{carta2.Spd}")
        print("--------------------------------------------------")

        # combate até alguém perder
        while carta1.Def > 0 and carta2.Def > 0:
            if carta1.Spd >= carta2.Spd:  
                # jogador ataca primeiro
                carta2.Def -= carta1.Atk
                if carta2.Def <= 0:
                    break
                carta1.Def -= carta2.Atk
            else:
                # inimigo ataca primeiro
                carta1.Def -= carta2.Atk
                if carta1.Def <= 0:
                    break
                carta2.Def -= carta1.Atk

        # resultado
        if carta1.Def > 0 and carta2.Def <= 0:
            print("================ JOGADOR VENCEU ================")
        elif carta2.Def > 0 and carta1.Def <= 0:
            print("================ ENEMY VENCEU =================")
        else:
            print("================ EMPATE =======================")

        
        print("//////////////////////////////////////////////////")


Adicionar()
Batalha()
















# for i in Fila:
#     print(f"NAME: {i.Name}")
#     print(f"ATK: {i.Atk}")
#     print(f"DEF: {i.Def}")
#     print(f"SPD: {i.Spd}")

# for i in Fila2:
#     print(f"NAME: {i.Name}")
#     print(f"ATK: {i.Atk}")
#     print(f"DEF: {i.Def}")
#     print(f"SPD: {i.Spd}")


# def Batalha():
#     competidores = []
#     while Fila or Fila2:
#         carta1 = Fila.pop(0)
#         carta2 = Fila2.pop(0)


#         while True:

#             if carta1.Spd > carta2.Spd:
#                 if carta2.Def - carta1.Atk < 1:
#                     print("===========================O Jogador Venceu===========================")
#                     print(f"JOGADOR: {carta1.Name}")
#                     print(f"ATK: {carta1.Atk}")
#                     print(f"DEF: {carta1.Def}")
#                     print(f"VEL: {carta1.Spd}")
#                     print("----------------------------------------------------------------------")
#                     print(f"ENEMY: {carta2.Name}")
#                     print(f"ATK: {carta2.Atk}")
#                     print(f"DEF: {carta2.Def}")
#                     print(f"VEL: {carta2.Spd}")
#                     print("///////////////////////////////////////////////////////////////////////")
#                     break
#                 else:
#                     carta1.Spd = 0
                    
#             else:
#                 if carta2.Spd > carta1.Spd:
#                     if carta1.Def - carta2.Atk < 1:
#                         print("===========================O Enemy Venceu===========================")
#                         print(f"JOGADOR: {carta1.Name}")
#                         print(f"ATK: {carta1.Atk}")
#                         print(f"DEF: {carta1.Def}")
#                         print(f"VEL: {carta1.Spd}")
#                         print("----------------------------------------------------------------------")
#                         print(f"ENEMY: {carta2.Name}")
#                         print(f"ATK: {carta2.Atk}")
#                         print(f"DEF: {carta2.Def}")
#                         print(f"VEL: {carta2.Spd}")
#                         print("///////////////////////////////////////////////////////////////////////")
#                         competidores = []
#                         acabou = True
#                     else:
#                         carta2.Spd = 0
                        
#                 else: 
#                     if carta1.Spd == 0 and carta2.Spd == 0:
#                         print("===========================Empatou Total mesmo===========================")
#                         print(f"JOGADOR: {carta1.Name}")
#                         print(f"ATK: {carta1.Atk}")
#                         print(f"DEF: {carta1.Def}")
#                         print(f"VEL: {carta1.Spd}")
#                         print("----------------------------------------------------------------------")
#                         print(f"ENEMY: {carta2.Name}")
#                         print(f"ATK: {carta2.Atk}")
#                         print(f"DEF: {carta2.Def}")
#                         print(f"VEL: {carta2.Spd}")
#                         print("///////////////////////////////////////////////////////////////////////")
#                         competidores = []
#                         break
                        




    
    # for i in range(5):
    #     if (Fila[i - 1].Def) - (Fila2[i - 1].Atk) > 0:
    #         if (Fila2[i - 1].Def) - (Fila[i - 1].Atk) > 0:
    #             print("=========================Empatou========================")
    #             print(f"JOGADOR: {Fila[i - 1].Name}")
    #             print(f"ATK: {Fila[i - 1].Atk}")
    #             print(f"DEF: {Fila[i - 1].Def}")
    #             print("--------------------------------------------------------")
    #             print(f"ENEMY: {Fila2[i - 1].Name}")
    #             print(f"ATK: {Fila2[i - 1].Atk}")
    #             print(f"DEF: {Fila2[i - 1].Def}")
    #             print("////////////////////////////////////////////////////////")
    #         else:
    #             print("======================Jogador Venceu====================")
    #             print(f"JOGADOR: {Fila[i - 1].Name}")
    #             print(f"ATK: {Fila[i - 1].Atk}")
    #             print(f"DEF: {Fila[i - 1].Def}")
    #             print("--------------------------------------------------------")
    #             print(f"ENEMY: {Fila2[i - 1].Name}")
    #             print(f"ATK: {Fila2[i - 1].Atk}")
    #             print(f"DEF: {Fila2[i - 1].Def}")
    #             print("////////////////////////////////////////////////////////")
    #     else:
    #         print("=======================Enemy Venceu=====================")
    #         print(f"JOGADOR: {Fila[i - 1].Name}")
    #         print(f"ATK: {Fila[i - 1].Atk}")
    #         print(f"DEF: {Fila[i - 1].Def}")
    #         print("--------------------------------------------------------")
    #         print(f"ENEMY: {Fila2[i - 1].Name}")
    #         print(f"ATK: {Fila2[i - 1].Atk}")
    #         print(f"DEF: {Fila2[i - 1].Def}")
    #         print("////////////////////////////////////////////////////////")



# for i in Pilha2:
#     print(f"NAME: {i.Name}")
#     print(f"ATK: {i.Atk}")
#     print(f"DEF: {i.Def}")
#     print(f"SPD: {i.Spd}")

# print(range(len(Pilha)))





