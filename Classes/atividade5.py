class Aluno:
    def __init__(self, id, nome=None, turma=None):
        self.id = id
        self.nome = nome
        self.turma = turma

    def imprimindo_dados(self):
        print(f"ID: {self.id}")
        if self.nome:
            print(f"Nome do Aluno: {self.nome}")
        if self.turma:
            print(f"Turma: {self.turma}")
        

