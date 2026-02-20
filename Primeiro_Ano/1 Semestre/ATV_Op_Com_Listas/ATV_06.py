nomes = ["Adriana", "Afonso", "Agatha", "Alana", "Alan", "Alessandra", "Alex", "Alice", "Aline", "Almir","Amanda", "Ana", "André", "Andressa", "Angela", "Antônio", "Ariana", "Artur", "Augusto", "Aurora","Beatriz", "Benício", "Bianca", "Breno", "Bruna", "Bruno", "Caio", "Camila", "Carlos", "Carolina","Cássia", "Catarina", "Célia", "César", "Clara", "Cláudia", "Cristiano", "Cíntia", "Célio", "Daniel","Daniele", "Danilo", "Davi", "Débora", "Denise", "Diego", "Diogo", "Douglas", "Eduarda", "Eduardo","Elaine", "Eliane", "Elisa", "Ellen", "Eloá", "Emerson", "Enzo", "Erick", "Estela", "Eva","Fabiana", "Fabrício", "Felipe", "Fernanda", "Fernando", "Flávia", "Francisco", "Gabriel", "Gabriela", "Geraldo","Giovana", "Gisele", "Guilherme", "Gustavo", "Heitor", "Helena", "Henrique", "Hugo", "Ian", "Igor","Isabela", "Isadora", "Israel", "Iuri", "Ivan", "Jacqueline", "Jaqueline", "Joana", "João", "Jonas","José", "Julia", "Juliana", "Júlio", "Karen", "Karina", "Kauã", "Kellen", "Kevin", "Kleber"]
nomes_minu = []
for x in nomes:
    nomes_minu.append(x.lower())

r1 = int(input("Digite o primeiro numero do range (0/99): "))
r2 = int(input("Digite o segundo numero do range (0/99): "))
nome = str(input("Digite o nome que procura: ")).lower()



for i in range(r1,r2):
    if nome == nomes_minu[i]:
        print(f"Achei {nome} no indice {i}")
        break
else:
    print(f"Nao achei esse tal de: {nome}")