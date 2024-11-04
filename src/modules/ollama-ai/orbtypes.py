from translate import translate as tlt
from enum import Enum
import time

class OrbTypes(Enum):
    Default = ""

def translate(type: OrbTypes):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/OrbTypes{game_type}.xml", f"game-data/mod/python/OrbTypes{game_type}.xml", "./OrbType/Name", context="Tipos de corpos celestes (estrelas, planetas, luas, etc)")

def execute():
    start_time = time.time()

    for enum in OrbTypes:
        translate(enum)

    print(f"{int((time.time() - start_time) / 60)}m")
