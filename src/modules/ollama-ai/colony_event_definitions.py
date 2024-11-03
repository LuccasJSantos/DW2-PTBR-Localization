from translate import translate as tlt
from enum import Enum
import time

class ColonyEventDefinitions(Enum):
    # Default = ""
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Governments = "Governments"
    # Human = "Human"
    # Ikkuro = "Ikkuro"
    # Mortalen = "Mortalen"
    # Quameno = "Quameno"
    Shakturi = "Shakturi"

def translate(type: ColonyEventDefinitions):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/ColonyEventDefinitions{game_type}.xml", f"game-data/transposition/ColonyEventDefinitions{game_type}.xml", "./ColonyEventDefinition/Name")
    tlt(f"game-data/transposition/ColonyEventDefinitions{game_type}.xml", f"game-data/transposition/ColonyEventDefinitions{game_type}.xml", "./ColonyEventDefinition/Description")

def execute():
    start_time = time.time()

    for enum in ColonyEventDefinitions:
        translate(enum)

    print(f"{int((time.time() - start_time) / 60)}m")

