import os
import ollama_parser as ollama

folders = [
    # { "source_path": "game-data/original/Galactopedia/GameConcepts", "target_path": "game-data/transposition/Galactopedia/GameConcepts" },
    { "source_path": "game-data/original/Galactopedia/GameScreens", "target_path": "game-data/transposition/Galactopedia/GameScreens" }
]

for folder in folders:
    files = os.listdir(folder['source_path'])

    for file in files:
        ollama.translate(f"{folder['source_path']}/{file}", f"{folder['target_path']}/{file}")
