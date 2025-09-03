from typing import Dict, Type, Callable

# Importando as classes base para que os Type Hints funcionem
from racas.raca_base import Raca
from classes.classe_base import Classe

# Importando as implementações de Raças e Classes
from racas.humano import Humano
from racas.anao import Anao
from racas.elfo import Elfo
from racas.halfling import Halfling
from classes.guerreiro import Guerreiro
from classes.ladrao import Ladrao
from classes.mago import Mago

# Outros imports
from personagem import Personagem
from gerador_atributos import GeradorAtributos


# Mapeamentos para seleção de Raça e Classe
RACAS_DISPONIVEIS: Dict[str, Type[Raca]] = {
    "1": Humano, "2": Anao, "3": Elfo, "4": Halfling
}
CLASSES_DISPONIVEIS: Dict[str, Type[Classe]] = {
    "1": Guerreiro, "2": Ladrao, "3": Mago
}

# Mapeamentos para geração de atributos
METODOS_ATRIBUTOS: Dict[str, Callable[[], Dict[str, int]]] = {
    "1": GeradorAtributos.gerar_classico,
    "2": GeradorAtributos.gerar_aventureiro,
    "3": GeradorAtributos.gerar_heroico,
}

# --- Funções de Seleção (Interface com o Usuário) ---

def selecionar_raca() -> Raca:
    """Apresenta as opções e retorna uma instância da Raça escolhida."""
    while True:
        print("\n--- Escolha a Raça do seu Personagem ---")
        for key, raca_classe in RACAS_DISPONIVEIS.items():
            print(f"{key}. {raca_classe().nome}")
        
        escolha = input("Digite o número da sua opção: ")
        if escolha in RACAS_DISPONIVEIS:
            return RACAS_DISPONIVEIS[escolha]()
        else:
            print("Opção inválida. Tente novamente.")

def selecionar_classe() -> Classe:
    """Apresenta as opções e retorna uma instância da Classe escolhida."""
    while True:
        print("\n--- Escolha a Classe do seu Personagem ---")
        for key, classe_obj in CLASSES_DISPONIVEIS.items():
            print(f"{key}. {classe_obj().nome}")
            
        escolha = input("Digite o número da sua opção: ")
        if escolha in CLASSES_DISPONIVEIS:
            return CLASSES_DISPONIVEIS[escolha]()
        else:
            print("Opção inválida. Tente novamente.")

def selecionar_atributos() -> Dict[str, int]:
    """Apresenta os métodos e retorna o dicionário de atributos gerados."""
    while True:
        print("\n--- Escolha o Método de Geração de Atributos ---")
        print("1. Clássico (3d6, em ordem)")
        print("2. Aventureiro (3d6, distribua os valores)")
        print("3. Heróico (4d6 drop lowest, distribua os valores)")
        
        escolha = input("Digite o número da sua opção: ")
        if escolha in METODOS_ATRIBUTOS:
            funcao_geradora = METODOS_ATRIBUTOS[escolha]
            return funcao_geradora()
        else:
            print("Opção inválida. Tente novamente.")

# --- Função Principal ---

def main():
    """Função principal que orquestra a criação do personagem."""
    print("=" * 40)
    print("Bem-vindo ao Criador de Personagens de Old Dragon!")
    print("=" * 40)

    nome_personagem = input("Primeiro, digite o nome do seu personagem: ")
    raca_escolhida = selecionar_raca()
    classe_escolhida = selecionar_classe()
    atributos_gerados = selecionar_atributos()

    personagem_final = Personagem(
        nome=nome_personagem,
        raca=raca_escolhida,
        classe=classe_escolhida,
        atributos=atributos_gerados
    )

    personagem_final.exibir_ficha()
    
    print("\nPersonagem criado com sucesso! Boa aventura!")

if __name__ == "__main__":
    main()