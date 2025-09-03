from .raca_base import Raca

class Anao(Raca):
    def __init__(self):
        super().__init__(
            nome="Anão",
            movimento=6,
            infravisao="18 metros",
            alinhamento="Tendência à Ordem"
        )

    def get_habilidades(self) -> dict:
        """
        Retorna as habilidades específicas do Anão.
        Fonte: Livro de Regras OD2, pág. 25.
        """
        return {
            "Mineradores": "Detecta anomalias em pedras, como armadilhas ou fossos escondidos.",
            "Vigoroso": "Recebe um bônus de +1 em qualquer teste de Jogada de Proteção de Constituição (JPC).",
            "Inimigos": "Ataques contra orcs, ogros e hobgoblins são considerados fáceis."
        }