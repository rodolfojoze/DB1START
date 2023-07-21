#digite os 3 lados de um triângula e descubra, se é isosceles, escaleno ou retâgulo

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("Os lados são iguais, é um triângulo equilátero")
elif lado1 != lado2 != lado3 !=lado1:
    print("Todos os lados são diferentes, é um triângulo escaleno!")
else:
    print("Dois lados iguais e um diferente, é um triângulo isósceles!")



#if lado1 == lado2 == lado3:
#   tipo_de_triangulo = "Equilátero"
#elif lado1 != lado2 != lado3 !=lado1:
#    tipo_de_triangulo = "Escaleno"
#else:
#   tipo_de_triangulo = "Isósceles"


