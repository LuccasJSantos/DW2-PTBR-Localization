from translate import translate as tlt
from enum import Enum
import time

class GameEvents(Enum):
    # Default = ""
    # Ancient_Guardian_Vaults = "Ancient_Guardian_Vaults"
    # Cell_Hegemony_Government = "Cell_Hegemony_Government"
    # Dhayut = "Dhayut"
    # Geniocracy_Government = "Geniocracy_Government"
    # Gizurean = "Gizurean"
    # Governments = "Governments"
    # HarmoniousUtopia_Government = "HarmoniousUtopia_Government"
    # Human = "Human"
    # Ikkuro_RaceEvents = "Ikkuro_RaceEvents"
    # Ikkuro = "Ikkuro"
    # Mortalen = "Mortalen"
    # Quameno = "Quameno"
    Shakturi_Vaults = "Shakturi_Vaults"
    Shakturi = "Shakturi"
    # SurveillanceOligarchy_Government = "SurveillanceOligarchy_Government"

def translate(type: GameEvents = ''):
    game_type = f"_{type.name}" if type != "" else ""

    # TriggerActions
    tlt(f"game-data/original/GameEvents{game_type}.xml", f"game-data/transposition/GameEvents{game_type}.xml", "./GameEvent/TriggerActions/GameEventAction/Description")
    tlt(f"game-data/transposition/GameEvents{game_type}.xml", f"game-data/transposition/GameEvents{game_type}.xml", "./GameEvent/TriggerActions/GameEventAction/MessageTitle")

    # PlacementActions
    tlt(f"game-data/transposition/GameEvents{game_type}.xml", f"game-data/transposition/GameEvents{game_type}.xml", "./GameEvent/PlacementActions/GameEventAction/Description")
    tlt(f"game-data/transposition/GameEvents{game_type}.xml", f"game-data/transposition/GameEvents{game_type}.xml", "./GameEvent/PlacementActions/GameEventAction/MessageTitle")

def execute():
    start_time = time.time()

    for enum in GameEvents:
        translate(enum)

    print(f"{int((time.time() - start_time) / 60)}m")
