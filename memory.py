import json
import os

MEMORY_FILE = "data/memory.json"

def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_memory(history):

    with open(MEMORY_FILE, "w") as file:
        json.dump(history, file, indent=4)