from dataclasses import dataclass
from racas.raca_base import Raca
from classes.classe_base import Classe
from typing import Dict

@dataclass
class Personagem:
    nome: str
    raca: Raca
    classe: Classe
    atributos: Dict[str, int]

    @property
    def pontos_de_vida(self) -> int:
        return self.classe.pontos_de_vida_inicial

    def exibir_ficha(self):
        """Exibe a ficha completa do personagem."""
        habilidades_raca = "\n".join([f"  - {nome}: {desc}" for nome, desc in self.raca.habilidades.items()])
        habilidades_classe = "\n".join([f"  - {nome}: {desc}" for nome, desc in self.classe.habilidades.items()])

        ficha = f"""
{'='*40}
FICHA DE PERSONAGEM
{'='*40}
Nome: {self.nome}
Raça: {self.raca.nome}
Classe: {self.classe.nome}
Alinhamento Padrão da Raça: {self.raca.alinhamento}

--- Atributos ---
Força: {self.atributos['Força']}
Destreza: {self.atributos['Destreza']}
Constituição: {self.atributos['Constituição']}
Inteligência: {self.atributos['Inteligência']}
Sabedoria: {self.atributos['Sabedoria']}
Carisma: {self.atributos['Carisma']}

--- Status de Combate ---
Pontos de Vida (PV): {self.pontos_de_vida}
Base de Ataque (BA): {self.classe.base_ataque}
Movimento: {self.raca.movimento}m
Infravisão: {self.raca.infravisao}

--- Habilidades de Raça ---
{habilidades_raca}

--- Habilidades de Classe (Nível 1) ---
{habilidades_classe}
{'='*40}
"""
        print(ficha)