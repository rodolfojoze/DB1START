#Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro

def multiplicandoNumeros(lista):
    if not lista:
        raise ValueError ("A lista não pode estar vazia.")
    
    multiplicaNaLista = int
   
    return multiplicaNaLista

lista1 = [5, 10, 5]
try:
    multiplicandoNumeros = multiplicaNaLista(lista1)
    print("A lista multiplicada é igual: ", multiplicandoNumeros)
except ValueError as e:
    print(e)



