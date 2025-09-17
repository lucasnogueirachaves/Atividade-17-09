class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        return f"Olá eu sou {self.nome} e tenho {self.idade} anos"

class Atleta(Pessoa):
    def __init__(self, nome, idade, modalidade):
        super().__init__(nome, idade)
        self.modalidade = modalidade

    def apresentar(self):
        info = super().apresentar()
        return f"{info}, eu sou da modalidade {self.modalidade}"

class Equipe(Atleta):
    def __init__(self, nome_equipe):
        self.nome_equipe = nome_equipe
        self.atletas = []
    
    def adicionar(self, atleta):
        self.atletas.append(atleta)
    def listar(self):
        for atleta in self.atletas:
            print(atleta.nome)
    def contar(self):
        print(len(self.atletas))

atleta1 = Atleta("Lucas", 19, "futebol")
atleta2 = Atleta("Ronaldo", 19, "futebol")
equip1 = Equipe("Flu")
equip1.adicionar(atleta1)
equip1.adicionar(atleta2)
equip1.listar()
equip1.contar()