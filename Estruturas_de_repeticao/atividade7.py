#Escreva um programa que solicite ao usuário um número inteiro positivo n e calcule a soma de todos os números inteiros de 1 até n.
def sum_of_intergers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def main():
    try:
        num = int(input("Digite um número inteiro positivo: ")) 
        if num <= 0:
            print("O número deve ser positivo.")
        else:
            result = sum_of_intergers(num)
            print("A soma dos números inteiros de 1 até", num, "é: ", result)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro positivo!")

if __name__ == "__main__":
    main()
    


    
