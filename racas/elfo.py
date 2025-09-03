from .raca_base import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__(
            nome="Elfo",
            movimento=9,
            infravisao="18 metros",
            alinhamento="Tendência à Neutralidade"
        )

    def get_habilidades(self) -> dict:
        """
        Retorna as habilidades específicas do Elfo.
        Fonte: Livro de Regras OD2, pág. 23.
        """
        return {
            "Percepção Natural": "Chance de detectar portas secretas mesmo sem procurar ativamente.",
            "Graciosos": "Recebe um bônus de +1 em qualquer teste de Jogada de Proteção de Destreza (JPD).",
            "Imunidades": "Imune a efeitos de sono e paralisia causada por Ghouls."
        }