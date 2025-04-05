from cx_Freeze import setup, Executable

# Configuração do executável
executables = [
    Executable("gui.py", target_name="Avacalc.exe")
]

# Configuração do cx_Freeze
setup(
    name="Avacalc",
    version="0.1.1",
    description="Calculador de Avaliações de Imóveis",
    options={
        "build_exe": {
            "packages": ["os"],  # Adicione os pacotes necessários
            "includes": ["avacalc", "codigos_sistema"],  # Inclua os módulos do projeto
            "include_files": []  # Arquivos adicionais (ex.: imagens, dados, etc.)
        }
    },
    executables=executables
)