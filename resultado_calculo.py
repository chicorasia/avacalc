"""Este arquivo define uma classe wrapper para encapsular resultado e descrição."""

class ResultadoCalculo:
    """Classe wrapper para encapsular o resultado e a descrição"""
    def __init__(self, codigo: str, descricao: str, valor_laudo_completo: float, valor_laudo_simplificado: float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_laudo_completo = valor_laudo_completo
        self.valor_laudo_simplificado = valor_laudo_simplificado

    def __str__(self):
        return (
            f"Código de sistema: {self.codigo}\n"
            f"Valor da OS laudo simplificado: R$ {self.valor_laudo_simplificado:.2f}\n"
            f"Valor da OS laudo completo: R$ {self.valor_laudo_completo:.2f}"
        )