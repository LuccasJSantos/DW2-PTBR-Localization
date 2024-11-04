from translate import translate as tlt
from enum import Enum
import time

class Artifacts(Enum):
    # Default = ""
    # AncientGuardianVaults = "AncientGuardianVaults"
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Ikkuro = "Ikkuro"
    # Quameno = "Quameno"
    Shakturi = "Shakturi"

def translate(type: Artifacts):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/Artifacts{game_type}.xml", f"game-data/transposition/Artifacts{game_type}.xml", "./Artifact/Name")
    tlt(f"game-data/transposition/Artifacts{game_type}.xml", f"game-data/transposition/Artifacts{game_type}.xml", "./Artifact/Description")

def execute():
    start_time = time.time()

    for enum in Artifacts:
        translate(enum)

    print(f"{int((time.time() - start_time) / 60)}m")

