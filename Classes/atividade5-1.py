from atividade5 import Aluno

aluno1 = Aluno(id=1)
aluno1.imprimindo_dados()
print("Tipo de classe.", type(aluno1))

aluno2 = Aluno(id=2, nome = "José")
aluno2.imprimindo_dados()
print("Atributos: ", aluno2.__dict__)

aluno3 = Aluno(id=3, nome = "Maria", turma = "A")
aluno3.imprimindo_dados()
print("Atributos:", aluno3.__dict__)
