from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Classe(ABC):
    nome: str
    pontos_de_vida_inicial: int
    base_ataque: int
    habilidades: Dict[str, str] = field(default_factory=dict, init=False)

    @abstractmethod
    def __post_init__(self):
        """Inicializa as habilidades da classe."""
        pass

    def __str__(self) -> str:
        return self.nome