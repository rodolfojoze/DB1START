class InvertendoString:
    def __init__(self):
        self.strings = []

    def adicionar_string(self, string):
        self.strings.append(string)
    
    def inverter_string(self):
        for string in self.strings: 
            inverted = string[::-1]
            print(f"A string original é: '{string}' e a string invertida é: '{inverted}'")


