from atividades1 import ConvertendoNumeroRomano

converter = ConvertendoNumeroRomano()

numero_romano = 3509
numero = converter.para_romano(numero_romano)
print(f"{numero_romano} em numeros romanos é: {numero}")

#converter = ConvertendoNumeroRomano()

numero_inteiro = "XV"
numero1 = converter.convertendo_string_to_int(numero_inteiro)
print(f"{numero_inteiro} em numeros inteiros é: {numero1}")