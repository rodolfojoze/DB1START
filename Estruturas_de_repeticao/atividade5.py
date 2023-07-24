#Faça um programa que leia 4 números e imprima o maior e o menor deles
def ler_numeros():
    numeros = []
    for i in range(4):
        numero = float(input(f"Digite o {i+1}º número! :"))
        numeros.append(numero)
    return numeros

def encontar_maior_menor(numeros):
    maior = menor = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor

def main():
    print("Digite 4 números: ")
    numeros = ler_numeros()
    maior, menor = encontar_maior_menor(numeros)
    print("O maior número é:", maior)
    print("O menor número é:", menor)

if __name__ == "__main__":
    main()

