#confira a média do aluno a partir de 3 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3= float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) /3
media_formatada = round(media, 2)
print(f"A média de notas do aluno é: {media_formatada:.2f}")    

