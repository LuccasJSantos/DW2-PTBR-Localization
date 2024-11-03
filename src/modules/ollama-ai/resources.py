from translate import translate as tlt
from enum import Enum
import time

class Resources(Enum):
    # Default = ""
    Shakturi = "Shakturi"

def translate(type: Resources):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/Resources{game_type}.xml", f"game-data/transposition/Resources{game_type}.xml", "./Resource/Name", context="Nome do recurso natural")
    tlt(f"game-data/transposition/Resources{game_type}.xml", f"game-data/transposition/Resources{game_type}.xml", "./Resource/Description", context="Descrição do recurso natural")

def execute():
    start_time = time.time()

    for enum in Resources:
        translate(enum)

    print(f"{((time.time() - start_time) / 60):.1f}min")
