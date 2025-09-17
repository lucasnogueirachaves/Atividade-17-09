class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        self.curso = curso
        super().__init__(nome, idade)

lucas = Estudante("Lucas", 19, "Computação")
print(lucas.__dict__)