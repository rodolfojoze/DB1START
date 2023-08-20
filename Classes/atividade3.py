class Exponenciacao:     
    def ler_numeros(self):
        self.base = float(input("Digite o número base:"))
        self.expoente = float(input("Digite o número expoente:"))
    
    def calculando_exponencial(self):
        self.resultado = pow(self.base, self.expoente)
    
    def mostrando_resultado(self):
        print(f"O resultado da exponenciação é: {self.resultado}")

    
    
   
