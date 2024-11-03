import os
from enum import Enum

def create_empty_file(file_path):
    if not os.path.exists(file_path):
        open(file_path, "w")

class TerminalColors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def fprint(text: str, color: TerminalColors):
    print(f"{color}{text}{TerminalColors.ENDC}")
