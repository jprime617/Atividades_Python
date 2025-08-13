from datetime import datetime, timedelta
import time

clientes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduardo"
]

fila = []



class Cliente :
    def __init__(self, nome, protocolo):
        self.nome = nome
        self.protocolo = protocolo
        self.hora_chegada = datetime.now()
        self.hora_atendimento = ""
        self.hora_saida = ""

class Caixa:
    def __init__(self, fila):
        self.fila = fila
    
    def atendimento(self):
        while self.fila:
            cliente.hora_atendimento = datetime.now()
            

        # for i, nome in enumerate(fila):
        #     time.sleep(2)
        #     print(nome.nome)
        #     fila.pop(i)
            
            


    def entrada():
        for i, nome in enumerate(clientes):
            fila.append(Cliente(nome, i))
            print(fila[i].nome, fila[i].protocolo, fila[i].hora_chegada)
            time.sleep(10)

    # def show_estado():


Caixa.entrada()
Caixa.atendimento()
