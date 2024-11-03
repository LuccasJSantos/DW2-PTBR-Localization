from translate import translate as tlt
from enum import Enum
import time

class PlanetaryFacilityDefinitions(Enum):
    # Default = ""
    # Ancient_Guardian_Vaults = "Ancient_Guardian_Vaults"
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Ikkuro = "Ikkuro"
    # Quameno = "Quameno"
    Shakturi = "Shakturi"

def translate(type: PlanetaryFacilityDefinitions):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/PlanetaryFacilityDefinitions{game_type}.xml", f"game-data/transposition/PlanetaryFacilityDefinitions{game_type}.xml", "./PlanetaryFacilityDefinition/Name", context="Nome de instalações planetárias")

def execute():
    start_time = time.time()

    for enum in PlanetaryFacilityDefinitions:
        translate(enum)

    print(f"{(time.time() - start_time) / 60}m")
