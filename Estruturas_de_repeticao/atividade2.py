#Faça um programa que peça as 4 notas bimestrais e mostre uma média indicando uma mensagem de reprovação caso a nota seja menor que 7
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 70:
    print("A média do aluno é:", media, "O aluno está APROVADO!")
else:
    print("A média do aluno é:", media, "O Aluno está REPROVADO!")
