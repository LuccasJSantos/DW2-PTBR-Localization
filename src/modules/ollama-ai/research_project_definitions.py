from translate import translate as tlt
from enum import Enum
import time

class ResearchProjectDefinitions(Enum):
    # Default = ""
    # Dhayut = "Dhayut"
    # Gizurean = "Gizurean"
    # Ikkuro = "Ikkuro"
    # Quameno = "Quameno"
    Shakturi = "Shakturi"

def translate(type: ResearchProjectDefinitions):
    game_type = f"_{type.value}" if type.value != "" else ""

    tlt(f"game-data/original/ResearchProjectDefinitions{game_type}.xml", f"game-data/transposition/ResearchProjectDefinitions{game_type}.xml", "./ResearchProjectDefinition/Name", context="Nome do projeto de pesquisa")
    tlt(f"game-data/transposition/ResearchProjectDefinitions{game_type}.xml", f"game-data/transposition/ResearchProjectDefinitions{game_type}.xml", "./ResearchProjectDefinition/DiplomacyFactors/EmpireIncidentFactor/Description", context="Descrição dos Fatores diplomáticos de incidentes do império")

def execute():
    start_time = time.time()

    for enum in ResearchProjectDefinitions:
        translate(enum)

    print(f"{((time.time() - start_time) / 60):.1f}min")
