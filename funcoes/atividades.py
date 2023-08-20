#def aplicar_desconto(valor, percentual): 
#    resultado = valor * (1 - (percentual / 100)) 
#    return resultado 

#valorOriginal = 25
#percentualDesconto = 10
#ValorComDesconto = aplicar_desconto(valorOriginal, percentualDesconto)
#print(ValorComDesconto)

def calcular_imc(peso: float, altura: float) -> float: 
    imc = peso / (altura ** 2) 

    return imc 

altura = 1.8
peso = 80
calculo_imc = calcular_imc(peso, altura)
print(calculo_imc)