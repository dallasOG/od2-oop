import random
from typing import List

def rolar_dados(quantidade: int, lados: int) -> List[int]:
    """Rola uma quantidade específica de dados com um número de lados."""
    return [random.randint(1, lados) for _ in range(quantidade)]

def rolar_4d6_drop_lowest() -> int:
    """Rola 4 dados de 6 lados e descarta o menor resultado."""
    rolagens = rolar_dados(4, 6)
    rolagens.sort()
    return sum(rolagens[1:])