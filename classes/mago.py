from .classe_base import Classe

class Mago(Classe):
    def __init__(self):
        super().__init__(nome="Mago", pontos_de_vida_inicial=4, base_ataque=0)

    def get_habilidades_de_classe(self) -> dict:
        """
        Retorna as habilidades específicas do Mago no 1º nível.
        """
        return {
            "Armas e Armaduras": "Limitado a armas pequenas e não pode usar armaduras.",
            "Magias Arcanas": "Pode lançar magias arcanas. Começa com 4 magias de 1º círculo no grimório.",
            "Ler Magias": "Pode decifrar inscrições mágicas.",
            "Detectar Magias": "Pode perceber a presença de magia em locais, pessoas ou objetos."
        }