from translate import translate as tlt
from enum import Enum
import time

class Governments(Enum):
    # Default = ""
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Ikkuro = "Ikkuro"
    # Quameno = "Quameno"
    Shakturi = "Shakturi"

def translate(type: Governments):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/Governments{game_type}.xml", f"game-data/transposition/Governments{game_type}.xml", "./Government/Name", context="Government Name")
    tlt(f"game-data/transposition/Governments{game_type}.xml", f"game-data/transposition/Governments{game_type}.xml", "./Government/Description", context="Government Description")
    tlt(f"game-data/transposition/Governments{game_type}.xml", f"game-data/transposition/Governments{game_type}.xml", "./Government/LeaderTitle", context="Government Leader Title")

def execute():
    start_time = time.time()

    for enum in Governments:
        translate(enum)

    print(f"{int((time.time() - start_time) / 60)}m")
