from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Raca(ABC):
    nome: str
    movimento: int
    infravisao: str
    alinhamento: str
    habilidades: Dict[str, str] = field(default_factory=dict, init=False)

    @abstractmethod
    def __post_init__(self):
        """Inicializa as habilidades da raça."""
        pass

    def __str__(self) -> str:
        return self.nome