#Escreva um programa que execute uma função que encontre o maior número de uma lista passada por parâmetro

def encontreMaiorNumero(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    
    maiorNumero = max(lista)    

    return maiorNumero

lista1 = [ 5, 50, 100, 2, 1000, 63]
maiorNumero = encontreMaiorNumero(lista1)
print("O maior número da lista é: ", maiorNumero)

lista2 = []
maiorNumero = encontreMaiorNumero(lista2)
print("O maior número da lista é: ", maiorNumero)

    

