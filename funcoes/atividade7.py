#Escreva um programa que execute uma função que conte o número de letras maiúsculas e minúsculas de um texto e que ao final chame outra função para
#imprimir o resultado

def MaisculaMinuscula(texto):
    contagemMaisculas = sum(1 for letra in texto if letra.isupper())
    contagemMinusculas = sum(1 for letra in texto if letra.islower())
    return contagemMaisculas, contagemMinusculas

def imprimindoResultado(contagemMaisculas, contagemMinusculas):
    print("A quantidade de letras maísculas no texto é de: ", contagemMaisculas)
    print("A quantidade de letras minusculas no texto é de: ", contagemMinusculas) 


def main():
    texto = input("Digite um texto aqui: ")
    contagemMaisculas, contagemMinusculas = MaisculaMinuscula(texto)
    imprimindoResultado(contagemMaisculas, contagemMinusculas)

if __name__ == "__main__":
    main()





   
    