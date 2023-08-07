#Escreva um programa que execute uma função que receba um número informado no console como
#parâmetro e verifique se o número informado é primo ou não

def numeroPrimo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        
        return True
    
numero1 = int(input("Digite um número: "))
if numeroPrimo(numero1):
    print("O número digitado", numero1, "é primo!")
else: 
    print("O número digitado", numero1, "não é primo!")
        


    