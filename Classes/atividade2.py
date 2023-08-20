class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
            'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
            'M': 1000
        }
        self.sorted_numerals = sorted(
            self.roman_numerals.keys(), key=lambda x: len(x), reverse=True
        )

    #def to_roman(self, num):
    #   # ...

    def from_roman(self, roman_numeral):
        result = 0
        i = 0
        while i < len(roman_numeral):
            for numeral in self.sorted_numerals:
                if roman_numeral[i:i+len(numeral)] == numeral:
                    result += self.roman_numerals[numeral]
                    i += len(numeral)
                    break
        return result

    def convert_string_to_int(self, roman_string):
        return self.from_roman(roman_string.upper())  # Converta para maiúsculas

# Teste a classe
converter = RomanConverter()
numero_romano = "MMCMXCIV"
numero = converter.convert_string_to_int(numero_romano)
print(f"{numero_romano} em algarismos indo-arábicos é: {numero}")

