import datetime

class JatoMilitar1Lugar():
    def __init__(self, modelo, base_inicial):
        self.modelo = modelo
        self.base_inicial = base_inicial
        self.piloto = None
        self.transferencias = []

    def designar_piloto(self, nome_piloto):
        self.piloto = nome_piloto

    def rebasear_aeronave(self, nova_base):
        if self.piloto:
            data_hora = datetime.datetime.now()
            self.transferencias.append((data_hora, nova_base))
        else:
            print("Não foi possível rebasear a nave, pois nenhum piloto foi designado.")

    def __str__ (self):
        info = f"Jato: {self.modelo}\nBase inicial: {self.base_inicial}\n"
        if self.piloto:
            info += f"Piloto: {self.piloto}\n"
        else: 
            info += f"Nenhum piloto foi designado.\n"

        if self.transferencias:
            info += "Histórico de transferências:\n"
            for data_hora, base in self.transferencias:
                info += f"{data_hora.strftime('%Y-%m-%d %H:%M:%S')} - {base}\n"
        else:
            info += "Nenhum histórico de transferência identificado.\n"

        return info






