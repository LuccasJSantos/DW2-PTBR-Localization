from translate import translate as tlt
from enum import Enum
import time

class SpaceItemDefinitions(Enum):
    # Default = ""
    Shakturi = "Shakturi"

def translate(type: Enum):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/SpaceItemDefinitions{game_type}.xml", f"game-data/transposition/SpaceItemDefinitions{game_type}.xml", "./SpaceItemDefinition/Name", context="Nome do item espacial")
    tlt(f"game-data/transposition/SpaceItemDefinitions{game_type}.xml", f"game-data/transposition/SpaceItemDefinitions{game_type}.xml", "./SpaceItemDefinition/Description", context="Descrição do item espacial")

def execute():
    start_time = time.time()

    for enum in SpaceItemDefinitions:
        translate(enum)

    print(f"{(time.time() - start_time) / 60}m")
