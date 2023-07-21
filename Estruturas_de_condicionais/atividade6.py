#uma listagem capturando os números e descrevendo-os em ordem decrescente.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

lista_numeros = [num1, num2, num3]
lista_numeros.sort(reverse=True)

print("Os números em ordem decrescente são: ")
for numero in lista_numeros:
    print(numero)

