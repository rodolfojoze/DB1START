def aprovado(nota1, nota2, nota3):
    mediaResultado = (nota1 + nota2 + nota3)  /3
    if mediaResultado >= 70:
        print("O aluno está aprovado")
    elif mediaResultado <= 69 and mediaResultado > 60:
        print("O aluno está de recuperação")
    elif mediaResultado < 59:
        print("O aluno está reprovado")
        
    return mediaResultado

nota_do_aluno1 = aprovado(80, 90, 90)
nota_do_aluno1_formatado = "{:.2f}".format(nota_do_aluno1)
print(nota_do_aluno1_formatado)

nota_do_aluno2 = aprovado(95, 45, 50)
nota_do_aluno2_formatado = "{:.2f}".format(nota_do_aluno2)
print(nota_do_aluno2_formatado)

nota_do_aluno3 = aprovado(50, 30, 90)
nota_do_aluno3_formatado = "{:.2f}".format(nota_do_aluno3)
print(nota_do_aluno3_formatado)

