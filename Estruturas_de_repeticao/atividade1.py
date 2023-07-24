#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês, e calcule o total do seu salário
por_hora = float(input("Digite o seu salário por hora: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalha por mês: "))

salario = por_hora * horas_trabalhadas 
print("O seu salário total é de:", salario)