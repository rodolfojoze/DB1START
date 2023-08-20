#Escreva uma classe em Python para converter um número inteiro em um numeral romano

class ConvertendoNumeroRomano:
    def __init__ (self): 
        self.roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 
        40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
        500: "D", 900: "CM", 1000: "M" 
    }
        
        self.sorted_numerals = sorted(
            self.roman_numerals.keys(), reverse = True
    )
    
    def para_romano(self, numero):
        resultado = ""
        for valor in self.sorted_numerals:
            while numero >= valor: 
                resultado += self.roman_numerals[valor]
                numero -= valor
        return resultado
    
    def de_romano(self, numeros_romanos):
        resultado = 0
        i = 0 
        while i < len(numeros_romanos):
            for numeral in self.sorted_numerals:
                if numeros_romanos[i:i + len(self.roman_numerals[numeral])] == self.roman_numerals[numeral]:
                    resultado += numeral
                    i += len(self.roman_numerals[numeral])
                    break
        return resultado
    
    def convertendo_string_to_int(self, roman_string):
       return self.de_romano(roman_string.upper())






