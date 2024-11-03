from translate import translate as tlt
from enum import Enum
import time

class CreatureTypes(Enum):
    # Default = ""
    Shakturi = "Shakturi"

def translate(type: CreatureTypes):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/CreatureTypes{game_type}.xml", f"game-data/transposition/CreatureTypes{game_type}.xml", "./CreatureType/Name")
    tlt(f"game-data/transposition/CreatureTypes{game_type}.xml", f"game-data/transposition/CreatureTypes{game_type}.xml", "./CreatureType/Description")

def execute():
    start_time = time.time()

    for enum in CreatureTypes:
        translate(enum)

    print(f"{int((time.time() - start_time) / 60)}m")

