from dataclasses import dataclass

@dataclass
class Livro:
    
    titulo: str
    autor: str
    ano: int
    preco: float

    def recente(self):
        if (2025 - self.ano) > 5:
            return "Saiu a mais de 5 anos"
        else:
            return "Saiu a menos de 5 anos"


    def caro(self):
        total = 0
        for livro in livros:
            total += livro.preco
        media = total / len(livros)
        if self.preco > media:
            return "Ta mais caro que a media"
        else:
            return "Ta mais barato que a media"
        
    


livros = [
    Livro("Jurassic Park", "Michael Crichton", 1990, 39.90),
    Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 49.90),
    Livro("O Senhor dos Anéis: As Duas Torres", "J.R.R. Tolkien", 1954, 49.90),
    Livro("O Senhor dos Anéis: O Retorno do Rei", "J.R.R. Tolkien", 1955, 49.90),
    Livro("Call of Cthulhu", "H.P. Lovecraft", 1928, 29.90),
    Livro("1984", "George Orwell", 1949, 34.90),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 24.90),
    Livro("Dom Quixote", "Miguel de Cervantes", 1605, 44.90),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 39.90),
    Livro("O Grande Gatsby", "F. Scott Fitzgerald", 1925, 29.90),
    Livro("Orgulho e Preconceito", "Jane Austen", 1813, 32.90),
    Livro("Mataram a Cotovia", "Harper Lee", 1960, 34.90),
    Livro("Crime e Castigo", "Fyodor Dostoiévski", 1866, 36.90),
    Livro("O Retrato de Dorian Gray", "Oscar Wilde", 1890, 28.90),
    Livro("A Metamorfose", "Franz Kafka", 1915, 26.90),
    Livro("O Processo", "Franz Kafka", 1925, 27.90),
    Livro("O Estrangeiro", "Albert Camus", 1942, 30.90),
    Livro("A Revolução dos Bichos", "George Orwell", 1945, 33.90),
    Livro("O Sol é para Todos", "Harper Lee", 1960, 31.90),
    Livro("O Hobbit", "J.R.R. Tolkien", 1937, 44.90),
    Livro("Do Dia para a Noite", "Bobbie Goods", 2025, 39.90),
    Livro("A Empregada", "Freida McFadden", 2025, 37.90),
    Livro("Verity", "Colleen Hoover", 2025, 42.90),
    Livro("A Coragem de Ser Imperfeito", "Brené Brown", 2015, 34.90),
    Livro("O Poder do Hábito", "Charles Duhigg", 2012, 29.90),
    Livro("Pai Rico, Pai Pobre", "Robert Kiyosaki", 1997, 28.90),
    Livro("O Milagre da Manhã", "Hal Elrod", 2012, 33.90),
    Livro("A Psicologia Financeira", "Morgan Housel", 2025, 38.90),
    Livro("A Biblioteca da Meia-Noite", "Matt Haig", 2020, 36.90),
    Livro("Ainda Estou Aqui", "Marcelo Rubens Paiva", 2025, 35.90),
    Livro("Amanhecer na Colheita", "Suzanne Collins", 2025, 41.90),
    Livro("Jantar Secreto", "Raphael Montes", 2025, 39.90),
    Livro("Em Busca de Sentido", "Viktor Frankl", 1946, 25.90),
    Livro("Hábitos Atômicos", "James Clear", 2018, 29.90),
    Livro("O Homem em Busca de Sentido", "Viktor Frankl", 1946, 25.90),
    Livro("O Poder do Agora", "Eckhart Tolle", 1997, 32.90),
    Livro("O Príncipe", "Nicolau Maquiavel", 1532, 21.90),
    Livro("O Cativeiro Babilônico da Igreja", "Martinho Lutero", 1520, 23.90),
    Livro("Gargantua e Pantagruel", "François Rabelais", 1532, 26.90),
    Livro("Institutas da Religião Cristã", "João Calvino", 1536, 27.90),
    Livro("O Primo Basílio", "José de Alencar", 1855, 29.90),
    Livro("Iracema", "José de Alencar", 1865, 28.90),
    Livro("Senhora", "José de Alencar", 1875, 27.90),
    Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 34.90),
    Livro("Dom Casmurro", "Machado de Assis", 1900, 33.90),
    Livro("A Moreninha", "Joaquim Manuel de Macedo", 1844, 25.90),
]

for livro in livros:
    print(f"O Livro: {livro.titulo} {livro.recente()} \n")


for livro in livros:
    print(f"O Livro: {livro.titulo} {livro.caro()} \n")


# recente(livros)
# caro(livros)


