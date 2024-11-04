from translate import translate as tlt
from enum import Enum
import time

class Races(Enum):
    # Default = ""
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Ikkuro = "Ikkuro"
    # Quameno = "Quameno"
    Shakturi = "Shakturi"

def translate(type: Races):
    game_type = f"_{type.value}" if type.value != "" else ""

    # tlt(f"game-data/original/Races{game_type}.xml", f"game-data/mod/python/Races{game_type}.xml", "./Race/FeatureExplanations/string", context="Explicação de funcionalidade da raça")
    tlt(f"game-data/original/Races{game_type}.xml", f"game-data/transposition/Races{game_type}.xml", "./Race/Name", context="Nome da raça")
    tlt(f"game-data/transposition/Races{game_type}.xml", f"game-data/transposition/Races{game_type}.xml", "./Race/Description", context="Descrição da raça")

def execute():
    start_time = time.time()

    for enum in Races:
        translate(enum)

    print(f"{((time.time() - start_time) / 60):.1f}min")
