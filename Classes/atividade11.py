import datetime

class JatoMilitar2Lugares:
    def __init__(self, modelo, base_inicial):
        self.modelo = modelo
        self.base_inicial = base_inicial
        self.pilotos = [None, None]
        self.transferencias = []

    def designar_piloto(self, nome_piloto):
        if None in self.pilotos:
            idx = self.pilotos.index(None)
            self.pilotos[idx] = nome_piloto
        else: 
            print("Dois pilotos já foram designados para essa aeronave.")       
        
    def rebasear_aerovane(self, nova_base):
        if None not in self.pilotos:
            data_hora = datetime.datetime.now()
            self.transferencias.append((data_hora, nova_base))
        else: 
            print("Não foi possível rebasear a aeronave, é necessário dois pilotos para continuar o processo.")

    def __str__(self):
        info = f"Jato: {self.modelo}\nBase inicial: {self.base_inicial}\n"
        pilotos = "\n".join([f"Piloto {i+1}: {piloto}" for i, piloto in enumerate(self.pilotos) if piloto is not None])
        info += pilotos + "\n"

        if self.transferencias: 
            info += "Histórico de transferência:\n"
            for data_hora, base in self.transferencias:
                info += f"{data_hora.strftime('%Y-%m-%d %H:%M:%S')} - {base}\n"
        else:
            print("Histórico de transferência: Nenhum histórico de transferência encontrado.")

        return info
            
        
