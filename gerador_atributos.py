from utils import rolar_dados, rolar_4d6_drop_lowest
from typing import Dict, List, Callable

class GeradorAtributos:
    ATRIBUTOS = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    @staticmethod
    def _distribuir_valores(rolagens: List[int]) -> Dict[str, int]:
        atributos = {}
        rolagens_disponiveis = rolagens[:]
        for atributo in GeradorAtributos.ATRIBUTOS:
            print(f"\nValores disponíveis: {rolagens_disponiveis}")
            while True:
                try:
                    escolha = int(input(f"Escolha um valor para {atributo}: "))
                    if escolha in rolagens_disponiveis:
                        atributos[atributo] = escolha
                        rolagens_disponiveis.remove(escolha)
                        break
                    else:
                        print("Valor inválido. Escolha um da lista de disponíveis.")
                except ValueError:
                    print("Por favor, digite um número válido.")
        return atributos

    @staticmethod
    def gerar_classico() -> Dict[str, int]:
        """Gera um dicionário de atributos no estilo Clássico."""
        print("Gerando atributos no Estilo Clássico...")
        return {atributo: sum(rolar_dados(3, 6)) for atributo in GeradorAtributos.ATRIBUTOS}

    @staticmethod
    def gerar_aventureiro() -> Dict[str, int]:
        """Gera um dicionário de atributos no estilo Aventureiro."""
        print("\nGerando atributos no Estilo Aventureiro...")
        rolagens = [sum(rolar_dados(3, 6)) for _ in range(6)]
        return GeradorAtributos._distribuir_valores(rolagens)

    @staticmethod
    def gerar_heroico() -> Dict[str, int]:
        """Gera um dicionário de atributos no estilo Heróico."""
        print("\nGerando atributos no Estilo Heróico...")
        rolagens = [rolar_4d6_drop_lowest() for _ in range(6)]
        return GeradorAtributos._distribuir_valores(rolagens)