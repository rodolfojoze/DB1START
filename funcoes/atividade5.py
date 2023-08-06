#Escreva um programa que execute uma função que retorne o inverso de uma string passada por parâmetro

def invertendoString(texto):
    return texto [::-1]

string1 = "Vamos lá!!"
stringInvertida = invertendoString(string1)
print("A string original é: ", string1)
print("A string invertida é: ", stringInvertida)

string2 = "!rodamargorp ednarg mu res uoV"
stringInvertida = invertendoString(string2)
print(stringInvertida)



