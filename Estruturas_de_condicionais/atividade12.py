#Digite uma data e verifique se ela é válida
data = input("Digite uma data no seguinte formato dd/mm/aaaa: ")

data_valida = True

dia, mes, ano = map(int, data.split('/'))

#verificando se o ano é bissexto 
if ano % 4 == 0 and (ano % 100 !=0 or ano % 400 ==0):
    dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#verificando se o mês é válido
if mes < 1 or mes > 12:
    data_valida = False

#verificando se o dia é válido
elif dia > 1 or dia > dias_por_mes[mes - 1]:
    data_valida = False

if data_valida:
  print("A data é válida")
else:
  print("A data é inválida")



