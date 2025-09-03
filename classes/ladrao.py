from .classe_base import Classe

class Ladrao(Classe):
    def __init__(self):
        super().__init__(nome="Ladrão", pontos_de_vida_inicial=6, base_ataque=1)

    def get_habilidades_de_classe(self) -> dict:
        """
        Retorna as habilidades específicas do Ladrão no 1º nível.
        """
        return {
            "Armas e Armaduras": "Limitado a armas pequenas/médias e armaduras leves.",
            "Ataque Furtivo": "Causa dano multiplicado por 2 ao atacar um inimigo de forma furtiva.",
            "Talentos de Ladrão": "Possui perícias em Armadilha, Arrombar, Escalar, Furtividade e Punga."
        }