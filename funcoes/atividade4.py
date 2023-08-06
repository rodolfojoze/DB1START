#Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro

def multiplicandoNumeros(lista):
    if not lista:
        raise ValueError ("A lista não pode estar vazia.")
    
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

lista1 = [1, 5, 10, 5]
resultadoMultiplicacao= multiplicandoNumeros(lista1)
print("O resultado da multiplicação a lista 1 inserida é: ", resultadoMultiplicacao)

lista2 = [5, 25, 6, 9, 12]
resultadoMultiplicacao= multiplicandoNumeros(lista2)
print("O resultado da multiplicação a lista 2 inserida é: ", resultadoMultiplicacao)

lista3 = []
resultadoMultiplicacao= multiplicandoNumeros(lista3)
print("O resultado da multiplicação a lista 3 inserida é: ", resultadoMultiplicacao)


    




