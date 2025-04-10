from enum import Enum

class ObjetoServico(Enum):
    IMOVEL = "Imovel"
    TERRENO_ATE_2000 = "Terreno com área até 2000 m2"
    TERRENO_ATE_10000 = "Terreno maior que 2000 m2 até 10000 m2"
    # TERRENO_MAIOR_QUE_10000 = "Terreno maior que 10000 m2"
