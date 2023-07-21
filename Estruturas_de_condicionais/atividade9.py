#descubra através de duas notas, se o aluno está aprovado, em recuperação ou aprovado
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2 

if media >= 70:
    print("O aluno está aprovado! Media:" , media)
elif media >= 60:
    print("O aluno está em recuperação! Media:", media)
elif media < 60:
    print("O Aluno está reprovado! Media: ", media)




