from dataclasses import dataclass
from .raca_base import Raca

@dataclass  # <--- REMOVED frozen=True
class Humano(Raca):
    nome: str = "Humano"
    movimento: int = 9
    infravisao: str = "Não possui"
    alinhamento: str = "Qualquer um"

    def __post_init__(self):
        # This line is now allowed because the dataclass is not frozen
        self.habilidades.update({
            "Aprendizado": "Recebe um bônus de 10% sobre toda experiência (XP) recebida.",
            "Adaptabilidade": "Recebe um bônus de +1 em uma única Jogada de Proteção à sua escolha."
        })