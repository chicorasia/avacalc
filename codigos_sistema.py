"""Esse arquivo concentra as definicoes de CodigoSistema e o dicionario
de configurações."""

from abc import ABC, abstractmethod

# define uma classe abstrata CodigoSistema
class CodigoSistema(ABC):
    """Essa classe abstrata define os comportamentos e atributos de um objeto Codigo de Sistema.
    Cada novo código deve herdar dessa classe. Cada nova implementação
    de CodigoSistema deve ser registrada no dicionário CONFIGURACOES.
    """

    # Dicionário centralizado com valores específicos para cada código
    CONFIGURACOES = {
        "A032": {"VALOR_BASE": 2096.00, "LIMITE_MAXIMO": 4056.00},
        "A037": {"VALOR_BASE": 3566.00, "LIMITE_MAXIMO": 4966.00},
        "A042": {"VALOR_BASE": 4466.00, "LIMITE_MAXIMO": 15000.00}
    }

    
    def __init__(self, codigo: str):
        if codigo not in self.CONFIGURACOES:
            raise ValueError(f"Código {codigo} não encontrado na configuração.")
        self.codigo = codigo
        self.valor_base = self.CONFIGURACOES[codigo]["VALOR_BASE"]
        self.limite_maximo = self.CONFIGURACOES[codigo]["LIMITE_MAXIMO"]

    
    @abstractmethod
    def calcular_valor(self, n: int, nt: int):
        pass

    def retorna_valor_ou_maximo(self, valor):
        """Compara o valor calculado com o LIMITE_MAXIMO para a classe
        e retorna o menor dos dois."""
        return min(valor, self.limite_maximo)


class A032(CodigoSistema):
    
    def __init__(self):
        super().__init__(codigo="A032")

    def calcular_valor(self, n, nt):
        valor = self.valor_base + 30 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor)    


class A037(CodigoSistema):
    
    def __init__(self):
        super().__init__(codigo="A037")

    def calcular_valor(self, n: int, nt: int):
        valor = self.valor_base + 18 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor) 


class A042(CodigoSistema):
   
    def __init__(self):
        super().__init__(codigo="A042")

    def calcular_valor(self, n: int, nt: int):
        valor = self.valor_base + 11 * (n - 1) + 20 * (nt - 1)
        return self.retorna_valor_ou_maximo(valor) 
