from atividade8 import Musica

estrofes_da_musica =[
    "Na bruma leve das paixões que vêm de dentro",
     "Tu vens chegando pra brincar no meu quintal",
     "No teu cavalo peito nu, cabelo ao vento",
     "E o sol quarando nossas roupas no varal (x2)\n"
]

estrofes_refrao= [
    "Tu vens, tu vens",
    "Eu já escuto os teus sinais",
    "Tu vens, tu vens",
    "Eu já escuto os teus sinais",

]
musica1 = Musica(estrofes_da_musica)
musica1.cante_para_mim()

musica2 = Musica(estrofes_refrao)
musica2.cante_para_mim()