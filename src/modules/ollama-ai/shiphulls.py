from translate import translate as tlt
from enum import Enum
import time

class ShipHulls(Enum):
    # Default = ""
    # Abandoned = "Abandoned"
    # Ackdarian = "Ackdarian"
    Berserk = "Berserk AI"
    # Boskara = "Boskara"
    # CrazedHiveInsectoids = "CrazedHiveInsectoids"
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Haakonish = "Haakonish"
    # Human = "Human"
    # Ikkuro = "Ikkuro"
    # Independant = "Independant"
    # Mortalen = "Mortalen"
    # Pirates1 = "Pirates1"
    # Pirates2 = "Pirates2"
    # Pirates3 = "Pirates3"
    # Pirates4 = "Pirates4"
    # PlanetDestroyer = "PlanetDestroyer"
    PlanetDestroyers = "PlanetDestroyers"
    # Quameno = "Quameno"
    Shakturi = "Shakturi"
    # Teekan = "Teekan"
    # Zenox = "Zenox"

def translate(type: Enum):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/ShipHulls{game_type}.xml", f"game-data/transposition/ShipHulls{game_type}.xml", "./ShipHull/Name", context="Nome do casco da nave")

def execute():
    start_time = time.time()

    for enum in ShipHulls:
        translate(enum)

    print(f"{(time.time() - start_time) / 60}m")
