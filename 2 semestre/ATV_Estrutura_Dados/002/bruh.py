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


for i in range(len(Pilha)):
    if len(Fila) < 5:

        Fila.append(Pilha.pop(-1))

for i in range(len(Pilha2)):
    if len(Fila2) < 5:

        Fila2.append(Pilha2.pop(-1))

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


def Batalha():
    competidores = []
    while Fila or Fila2:
        competidores.append(Fila.pop(0))
        competidores.append(Fila2.pop(0))

        if competidores[0].Spd > competidores[1].Spd:
            if competidores[1].Def - competidores[0].Atk < 1:
                print("===========================O Jogador Venceu===========================")
                print(f"JOGADOR: {competidores[0].Name}")
                print(f"ATK: {competidores[0].Atk}")
                print(f"DEF: {competidores[0].Def}")
                print(f"VEL: {competidores[0].Spd}")
                print("----------------------------------------------------------------------")
                print(f"ENEMY: {competidores[1].Name}")
                print(f"ATK: {competidores[1].Atk}")
                print(f"DEF: {competidores[1].Def}")
                print(f"VEL: {competidores[1].Spd}")
                print("///////////////////////////////////////////////////////////////////////")
                competidores = []
            else:
                if competidores[0].Def - competidores[1].Atk < 1:
                    print("===========================O Enemy Venceu===========================")
                    print(f"JOGADOR: {competidores[0].Name}")
                    print(f"ATK: {competidores[0].Atk}")
                    print(f"DEF: {competidores[0].Def}")
                    print(f"VEL: {competidores[0].Spd}")
                    print("----------------------------------------------------------------------")
                    print(f"ENEMY: {competidores[1].Name}")
                    print(f"ATK: {competidores[1].Atk}")
                    print(f"DEF: {competidores[1].Def}")
                    print(f"VEL: {competidores[1].Spd}")
                    print("///////////////////////////////////////////////////////////////////////")
                    competidores = []
                else:
                    print("===========================Empatou / Jogador===========================")
                    print(f"JOGADOR: {competidores[0].Name}")
                    print(f"ATK: {competidores[0].Atk}")
                    print(f"DEF: {competidores[0].Def}")
                    print(f"VEL: {competidores[0].Spd}")
                    print("----------------------------------------------------------------------")
                    print(f"ENEMY: {competidores[1].Name}")
                    print(f"ATK: {competidores[1].Atk}")
                    print(f"DEF: {competidores[1].Def}")
                    print(f"VEL: {competidores[1].Spd}")
                    print("///////////////////////////////////////////////////////////////////////")
                    competidores[0].Spd = 0
        else:
            if competidores[1].Spd > competidores[0].Spd:
                if competidores[0].Def - competidores[1].Atk < 1:
                    print("===========================O Enemy Venceu===========================")
                    print(f"JOGADOR: {competidores[0].Name}")
                    print(f"ATK: {competidores[0].Atk}")
                    print(f"DEF: {competidores[0].Def}")
                    print(f"VEL: {competidores[0].Spd}")
                    print("----------------------------------------------------------------------")
                    print(f"ENEMY: {competidores[1].Name}")
                    print(f"ATK: {competidores[1].Atk}")
                    print(f"DEF: {competidores[1].Def}")
                    print(f"VEL: {competidores[1].Spd}")
                    print("///////////////////////////////////////////////////////////////////////")
                    competidores = []
                else:
                    if competidores[1].Def - competidores[0].Atk < 1:
                        print("===========================O Jogador Venceu===========================")
                        print(f"JOGADOR: {competidores[0].Name}")
                        print(f"ATK: {competidores[0].Atk}")
                        print(f"DEF: {competidores[0].Def}")
                        print(f"VEL: {competidores[0].Spd}")
                        print("----------------------------------------------------------------------")
                        print(f"ENEMY: {competidores[1].Name}")
                        print(f"ATK: {competidores[1].Atk}")
                        print(f"DEF: {competidores[1].Def}")
                        print(f"VEL: {competidores[1].Spd}")
                        print("///////////////////////////////////////////////////////////////////////")
                        competidores = []
                    else:
                        print("===========================Empatou / Enemy===========================")
                        print(f"JOGADOR: {competidores[0].Name}")
                        print(f"ATK: {competidores[0].Atk}")
                        print(f"DEF: {competidores[0].Def}")
                        print(f"VEL: {competidores[0].Spd}")
                        print("----------------------------------------------------------------------")
                        print(f"ENEMY: {competidores[1].Name}")
                        print(f"ATK: {competidores[1].Atk}")
                        print(f"DEF: {competidores[1].Def}")
                        print(f"VEL: {competidores[1].Spd}")
                        print("///////////////////////////////////////////////////////////////////////")
                        competidores[1].Spd = 0
            else: 
                if competidores[0].Spd == 0 and competidores[1].Spd == 0:
                    print("===========================Empatou Total mesmo===========================")
                    print(f"JOGADOR: {competidores[0].Name}")
                    print(f"ATK: {competidores[0].Atk}")
                    print(f"DEF: {competidores[0].Def}")
                    print(f"VEL: {competidores[0].Spd}")
                    print("----------------------------------------------------------------------")
                    print(f"ENEMY: {competidores[1].Name}")
                    print(f"ATK: {competidores[1].Atk}")
                    print(f"DEF: {competidores[1].Def}")
                    print(f"VEL: {competidores[1].Spd}")
                    print("///////////////////////////////////////////////////////////////////////")
                    competidores = []




    
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


Batalha()



# for i in Pilha2:
#     print(f"NAME: {i.Name}")
#     print(f"ATK: {i.Atk}")
#     print(f"DEF: {i.Def}")
#     print(f"SPD: {i.Spd}")

# print(range(len(Pilha)))





