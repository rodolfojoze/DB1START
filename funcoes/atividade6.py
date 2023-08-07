#Escreva um programa que execute uma função que calcule o fatorial de um número passado por parâmetro

def calculandoFatorial(numero):
    if numero < 0:
        return None
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial


numero1 = 4
resultado = calculandoFatorial(numero1)
print("O valor fatorial do número 1 é:", resultado)

numero2 = 0
resultado = calculandoFatorial(numero2)
print("O valor fatorial do número 2 é:",resultado)

numero3 = -5
resultado = calculandoFatorial(numero3)
print("O valor fatorial do número 3 é:",resultado)



    