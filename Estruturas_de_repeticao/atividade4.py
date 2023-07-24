#Faça um programa que peça 3 números e imprima o maior deles
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 > num3:
    print("O maior número digitado é o primeiro:", num1)
elif num2 > num1 > num3:
    print("O maior número digitado é o segundo:", num2)
else:
    print("O maior número digitado é o terceiro:", num3)
