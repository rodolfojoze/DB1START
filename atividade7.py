#Faça um programa que leia um número e exiba o dia correspondente da semana
numero = int(input("Digite o número do dia da semana: "))

if numero == 1:
    dia_da_semana = "Domingo" 
#    print("Domingo")
elif numero == 2:
    dia_da_semana = "Segunda-feira"
#    print("Segunda-feira")
elif numero == 3:
    dia_da_semana = "Terça-feira"
#    print("Terça-feira")
elif numero == 4:
    dia_da_semana = "Quarta-feira"
#    print("Quarta-feira")
elif numero == 5:
    dia_da_semana = "Quinta-feira"
#    print("Quinta-feira")
elif numero == 6:
    dia_da_semana = "Sexta-feira"
#    print("Sexta-feira")
elif numero == 7:
    dia_da_semana = "Sábado"
#   print("Sábado")
else:
    dia_da_semana = "Valor inválido"
#   print("Número digitado inválido")

print("O dia correspondente é: ", dia_da_semana)