"""Uma classe genérica para manter estados"""

from typing import TypeVar, Generic

T = TypeVar('T')

class Estado(Generic[T]):
    def __init__(self, estado_inicial: T):
        self.estado = estado_inicial

    def definir_estado(self, novo_estado: T):
        self.estado = novo_estado
        
    def obter_estado(self) -> T:
        return self.estado