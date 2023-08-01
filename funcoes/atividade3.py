#Escreva um programa que execute uma função que some todos os itens de uma lista passada por parâmetro

def somaLista(lista):
    if not lista:
       raise ValueError("A lista não pode estar vazia.")
    
    numerosSomados = sum(lista)

    return numerosSomados

lista1 = [1, 25, 26, 52, 63]
numerosSomados = somaLista(lista1)
print("A soma dos números da lista é igual: ", numerosSomados)

lista2 = []
numerosSomados = somaLista(lista2)
print("A soma dos números da lista é igual: ", numerosSomados)



