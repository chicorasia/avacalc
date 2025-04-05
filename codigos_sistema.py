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
        "A030": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* até 50 unidades). Avaliação de imóveis novos ou terrenos com características similares.",
        "A032": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* até 50 unidades). Avaliação de imóveis por situação paradigma.",
        "A035": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* entre 51 e 100 unidades). Avaliação de imóveis novos ou terrenos com características similares.",
        "A037": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* entre 51 e 100 unidades). Avaliação de imóveis por situação paradigma.",
        "A040": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* acima de 100 unidades). Avaliação de imóveis novos ou terrenos com características similares.",
        "A042": "Conjunto de imóveis urbanos do Grupo 1, no mesmo empreendimento, ou com características assemelhadas numa mesma região (Empreendimentos ou conjunto de unidades assemelhadas com n* acima de 100 unidades). Avaliação de imóveis por situação paradigma."
    }

    # Dicionário centralizado com valores específicos para cada código
    CONFIGURACOES = {
        "A030": {"VALOR_BASE_LAUDO_SIMPLIFICADO": 699.00, "VALOR_BASE_LAUDO_COMPLETO": 1572.00, "LIMITE_MAXIMO": 5247.00, "DESCRICAO": DESCRICOES["A030"]},
        "A032": {"VALOR_BASE_LAUDO_SIMPLIFICADO": 923.00, "VALOR_BASE_LAUDO_COMPLETO": 2096.00, "LIMITE_MAXIMO": 4056.00, "DESCRICAO": DESCRICOES["A032"]},
        "A035": {"VALOR_BASE_LAUDO_SIMPLIFICADO": 2169.00, "VALOR_BASE_LAUDO_COMPLETO": 3042.00, "LIMITE_MAXIMO": 6192.00, "DESCRICAO": DESCRICOES["A035"]},
        "A037": {"VALOR_BASE_LAUDO_SIMPLIFICADO": 2402.00, "VALOR_BASE_LAUDO_COMPLETO": 3566.00, "LIMITE_MAXIMO": 4966.00, "DESCRICAO": DESCRICOES["A037"]},
        "A040": {"VALOR_BASE_LAUDO_SIMPLIFICADO": 3069.00, "VALOR_BASE_LAUDO_COMPLETO": 3942.00, "LIMITE_MAXIMO": 20000.00, "LIMITE_MAXIMO_2": 25000.00,"DESCRICAO": DESCRICOES["A040"]},
        "A042": {"VALOR_BASE_LAUDO_SIMPLIFICADO": 3302.00, "VALOR_BASE_LAUDO_COMPLETO": 4466.00, "LIMITE_MAXIMO": 15000.00, "DESCRICAO": DESCRICOES["A042"]}
    }

    
    def __init__(self, codigo: str):
        if codigo not in self.CONFIGURACOES:
            raise ValueError(f"Código {codigo} não encontrado na configuração.")
        self.codigo = codigo
        self.valor_base_completo = self.CONFIGURACOES[codigo]["VALOR_BASE_LAUDO_COMPLETO"]
        self.valor_base_simplificado = self.CONFIGURACOES[codigo]["VALOR_BASE_LAUDO_SIMPLIFICADO"]
        self.limite_maximo = self.CONFIGURACOES[codigo]["LIMITE_MAXIMO"]
        self.descricao = self.DESCRICOES[codigo]

    
    @abstractmethod
    def calcular_valor_laudo_simplificado(self, n: int, nt: int):
        """Calcula o valor da OS com base em laudo simplificado"""
        pass

    @abstractmethod
    def calcular_valor_laudo_completo(self, n: int, nt: int):
        """Calcula o valor da OS com base em laudo completo"""
        pass

    def retorna_valor_ou_maximo(self, valor):
        """Compara o valor calculado com o LIMITE_MAXIMO para a classe
        e retorna o menor dos dois."""
        return min(valor, self.limite_maximo)


class A030(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, n* até 50 unidades).
    Avaliação de imóveis novos ou terrenos com caracteristicas similares.
    """
    def __init__(self):
        super().__init__(codigo="A030")

    def calcular_valor_laudo_completo(self, n, nt, nl = 1, nv = 1):
        """Considera valor padrão 1 para nl e nv"""
        valor = self.valor_base_completo + 30 * (n - 1) + 10 * (nt - 1) + 20 * (nl - 1) + 15 * (nv - 1)
        return self.retorna_valor_ou_maximo(valor)
    
    def calcular_valor_laudo_simplificado(self, n, nt, nl = 1, nv = 1):
        valor = self.valor_base_simplificado + 30 * (n - 1) + 10 * (nt - 1) + 10 * (nl - 1) + 15 * (nv - 1)
        return self.retorna_valor_ou_maximo(valor)



class A032(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, n* até 50 unidades).
    Avaliação de imóveis por situação paradigma.
    """
    
    def __init__(self):
        super().__init__(codigo="A032")

    def calcular_valor_laudo_completo(self, n, nt):
        valor = self.valor_base_completo + 30 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)
    
    def calcular_valor_laudo_simplificado(self, n, nt):
        valor = self.valor_base_simplificado + 30 * (n - 1) + 10 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)


class A035(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, de 51 até 100 unidades).
    Avaliação de imóveis novos ou terrenos com caracteristicas similares.
    """
    
    def __init__(self):
        super().__init__(codigo="A035")

    def calcular_valor_laudo_completo(self, n, nt, nl = 1, nv = 1):
        """Considera valor padrão 1 para nl e nv"""
        valor = self.valor_base_completo + 18 * (n - 1) + 10 * (nt - 1) + 10 * (nl - 1) + 15 * (nv - 1)
        return self.retorna_valor_ou_maximo(valor)
    
    def calcular_valor_laudo_simplificado(self, n, nt, nl = 1, nv = 1):
        valor = self.valor_base_simplificado + 18 * (n - 1) + 10 * (nt - 1) + 10 * (nl - 1) + 15 * (nv - 1)
        return self.retorna_valor_ou_maximo(valor)


class A037(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, n* de 51 até 100 unidades).
    Avaliação de imóveis por situação paradigma.
    """
    
    def __init__(self):
        super().__init__(codigo="A037")

    def calcular_valor_laudo_completo(self, n: int, nt: int):
        valor = self.valor_base_completo + 18 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)
    
    def calcular_valor_laudo_simplificado(self, n, nt):
        valor = self.valor_base_simplificado + 18 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)


class A040(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, acima de 100 unidades).
    Avaliação de imóveis novos ou terrenos com caracteristicas similares.
    """
    
    def __init__(self):
        super().__init__(codigo="A040")

    def calcular_valor_laudo_completo(self, n, nt, nl = 1, nv = 1):
        """Considera valor padrão 1 para nl e nv"""
        valor = self.valor_base_completo + 18 * (n - 1) + 10 * (nt - 1) + 20 * (nl - 1) + 15 * (nv - 1)
        # Excepcionalidade dessa regra de cálculo
        return min(valor, self.CONFIGURACOES["A040"]["LIMITE_MAXIMO_2"])
    
    def calcular_valor_laudo_simplificado(self, n, nt, nl = 1, nv = 1):
        valor = self.valor_base_simplificado + 11 * (n - 1) + 10 * (nt - 1) + 10 * (nl - 1) + 15 * (nv - 1)
        return self.retorna_valor_ou_maximo(valor)


class A042(CodigoSistema):
    """Conjunto de imóveis urbanos do Grupo 1, n* acima de 100 unidades).
    Avaliação de imóveis por situação paradigma.
    """
   
    def __init__(self):
        super().__init__(codigo="A042")

    def calcular_valor_laudo_completo(self, n: int, nt: int):
        valor = self.valor_base_completo + 11 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)
    
    def calcular_valor_laudo_simplificado(self, n, nt):
        valor = self.valor_base_simplificado + 11 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)

