from .raca_base import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__(
            nome="Halfling",
            movimento=6,
            infravisao="Não possui",
            alinhamento="Tendência à Neutralidade"
        )

    def get_habilidades(self) -> dict:
        """
        Retorna as habilidades específicas do Halfling.
        Fonte: Livro de Regras OD2, pág. 27.
        """
        return {
            "Furtivos": "Especialistas em se esconder e passar despercebidos, com bônus para a classe Ladrão.",
            "Destemidos": "Recebe um bônus de +1 em qualquer teste de Jogada de Proteção de Sabedoria (JPS).",
            "Bons de Mira": "Qualquer ataque à distância com uma arma de arremesso é considerado um ataque fácil.",
            "Pequenos": "Ataques de criaturas grandes ou maiores são difíceis de acertar um Halfling."
        }