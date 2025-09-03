from .classe_base import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__(nome="Guerreiro", pontos_de_vida_inicial=10, base_ataque=1)

    def get_habilidades_de_classe(self) -> dict:
        """
        Retorna as habilidades específicas do Guerreiro no 1º nível.
        """
        return {
            "Armas e Armaduras": "Pode usar todas as armas e armaduras.",
            "Aparar": "Pode sacrificar um escudo ou arma para absorver todo o dano de um ataque.",
            "Maestria em Arma": "No 1º nível, escolhe uma arma para ser mestre, recebendo +1 de bônus no dano com ela."
        }