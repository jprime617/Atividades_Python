from dataclasses import dataclass
import random

@dataclass
class Aluno:
    nome: str
    idade: int
    media: float

    def aprovado(self):
        if self.media >= 7:
            return "Passou"
        else:
            return "Não Passou"



aluno = Aluno("Felipe", 16, round(random.uniform(0,10),1))

# aluno = Aluno("Felipe", 16, 7.6)  # CRIAR
# print(aluno.nome)               # EXIBIR
# aluno.nota = 8.7                # ALTERAR

print(f"NOME: {aluno.nome}")
print(f"IDADE: {aluno.idade}")
print(f"MEDIA: {aluno.media}")
print(aluno.aprovado())


# class Aluno:
#     def __init__(self, nome, idade, media):
#         self.nome = nome
#         self.idade = idade
#         self.media = media

#     def aprovado(self):
#         return self.media >= 7.0
    

