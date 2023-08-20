class AlunoIdAutomatica:
    contador_id = 0       

    def __init__(self, nome=None, turma=None):
        AlunoIdAutomatica.contador_id += 1
        self.id = AlunoIdAutomatica.contador_id
        self.nome = nome
        self.turma = turma

    def imprimindo_dados(self):
        print(f"ID: {self.id}")
        if self.nome:
            print(f"Nome do Aluno: {self.nome}")
        if self.turma:
            print(f"Turma: {self.turma}")

