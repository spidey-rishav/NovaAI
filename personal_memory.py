import json
import os

FILE = "data/personal_memory.json"

def load_personal_memory():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)

def save_personal_memory(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def remember_fact(key, value):

    memory = load_personal_memory()

    memory[key] = value

    save_personal_memory(memory)

def get_fact(key):

    memory = load_personal_memory()

    return memory.get(key)