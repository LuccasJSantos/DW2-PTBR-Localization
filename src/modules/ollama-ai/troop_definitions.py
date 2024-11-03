from translate import translate as tlt
from enum import Enum
import time

class TroopDefinitions(Enum):
    # Default = ""
    Shakturi = "Shakturi"

def translate(type: Enum):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/TroopDefinitions{game_type}.xml", f"game-data/transposition/TroopDefinitions{game_type}.xml", "./TroopDefinition/Name", context="Nome da tropa")
    tlt(f"game-data/transposition/TroopDefinitions{game_type}.xml", f"game-data/transposition/TroopDefinitions{game_type}.xml", "./TroopDefinition/Description", context="Descrição da tropa")

def execute():
    start_time = time.time()

    for enum in TroopDefinitions:
        translate(enum)

    print(f"{(time.time() - start_time) / 60}m")
