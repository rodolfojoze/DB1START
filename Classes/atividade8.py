#Criar uma classe Musica, que deverá receber como parâmetro de criação uma lista de string com as
#estrofes de uma música. Essa classe deverá conter um método chamado cante_para_mim que imprima
#todas as estrofes, uma em cada linha. Para executar instancie a classe e execute o método

class Musica:
    def __init__(self, estrofes):
        self.estrofes = estrofes

    def cante_para_mim(self):
        for estrofes in self.estrofes: 
            print(estrofes)


