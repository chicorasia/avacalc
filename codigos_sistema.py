"""Esse arquivo concentra as definicoes de CodigoSistema e o dicionario
de configurações."""

from abc import ABC, abstractmethod

# define uma classe abstrata CodigoSistema
class CodigoSistema(ABC):
    """Essa classe abstrata define os comportamentos e atributos de um objeto Codigo de Sistema.
    Cada novo código deve herdar dessa classe. Cada nova implementação
    de CodigoSistema deve ser registrada nos dicionários DESCRICOES e
    CONFIGURACOES.
    """

    # Dicionário com descrições separadas
    DESCRICOES = {
        "A032": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* até 50 unidades). Avaliação de imóveis por situação paradigma. Laudo completo.",
        "A037": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* entre 51 e 100 unidades). Avaliação de imóveis por situação paradigma. Laudo completo.",
        "A042": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* acima de 100 unidades). Avaliação de imóveis por situação paradigma. Laudo completo."
    }

    # Dicionário centralizado com valores específicos para cada código
    CONFIGURACOES = {
        "A032": {"VALOR_BASE": 2096.00, "LIMITE_MAXIMO": 4056.00, "DESCRICAO": DESCRICOES["A032"]},
        "A037": {"VALOR_BASE": 3566.00, "LIMITE_MAXIMO": 4966.00, "DESCRICAO": DESCRICOES["A037"]},
        "A042": {"VALOR_BASE": 4466.00, "LIMITE_MAXIMO": 15000.00, "DESCRICAO": DESCRICOES["A042"]}
    }

    
    def __init__(self, codigo: str):
        if codigo not in self.CONFIGURACOES:
            raise ValueError(f"Código {codigo} não encontrado na configuração.")
        self.codigo = codigo
        self.valor_base = self.CONFIGURACOES[codigo]["VALOR_BASE"]
        self.limite_maximo = self.CONFIGURACOES[codigo]["LIMITE_MAXIMO"]
        self.descricao = self.DESCRICOES[codigo]

    
    @abstractmethod
    def calcular_valor(self, n: int, nt: int):
        pass

    def retorna_valor_ou_maximo(self, valor):
        """Compara o valor calculado com o LIMITE_MAXIMO para a classe
        e retorna o menor dos dois."""
        return min(valor, self.limite_maximo)


class A032(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, n* até 50 unidades).
    Avaliação de imóveis por situação paradigma. Laudo completo.
    """
    
    def __init__(self):
        super().__init__(codigo="A032")

    def calcular_valor(self, n, nt):
        valor = self.valor_base + 30 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)    


class A037(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, n* até de 51 até 100 unidades).
    Avaliação de imóveis por situação paradigma. Laudo completo.
    """
    
    def __init__(self):
        super().__init__(codigo="A037")

    def calcular_valor(self, n: int, nt: int):
        valor = self.valor_base + 18 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor) 


class A042(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, n* acima de 100 unidades).
    Avaliação de imóveis por situação paradigma. Laudo completo.
    """
   
    def __init__(self):
        super().__init__(codigo="A042")

    def calcular_valor(self, n: int, nt: int):
        valor = self.valor_base + 11 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor) 
