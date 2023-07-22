#Escreva um numero até 1000 e escreva as casas de unidades, dezenas e centenas.
num = int(input("Digite um número inteiro até 1000! "))

if num < 1000 and num > 0:
    centenas = num // 100
    dezenas = (num  % 100) // 10
    unidades = (num % 100) % 10

    print("Centenas", centenas)
    print("Dezenas", dezenas)
    print("Unidades", unidades)

else:
  print("O número digitado é inválido")







