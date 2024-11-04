from translate import translate as tlt
from enum import Enum
import time

class ComponentDefinitions(Enum):
    # Default = ""
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Ikkuro = "Ikkuro"
    # PlanetDestroyers = "PlanetDestroyers"
    # Quameno = "Quameno"
    PlanetDestroyers = "PlanetDestroyers"
    Shakturi = "Shakturi"

def translate(type: ComponentDefinitions):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/ComponentDefinitions{game_type}.xml", f"game-data/transposition/ComponentDefinitions{game_type}.xml", "./ComponentDefinition/Name")

def execute():
    start_time = time.time()

    for enum in ComponentDefinitions:
        translate(enum)

    print(f"{int((time.time() - start_time) / 60)}m")

