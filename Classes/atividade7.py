class Triangulo:
    def __init__ (self, angulo1, angulo2, angulo3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3

    def check_angulo(self):
        return self.angulo1 + self.angulo2 + self.angulo3 == 180
    
    def impressao (self):
        print(f"O ângulo 1 : {self.angulo1}")
        print(f"O ângulo 2 : {self.angulo2}")
        print(f"O ângulo 3 : {self.angulo3}")
        if self.check_angulo():
            print("É um triângulo válido")
        else:
            print("Não é um triângulo válido")