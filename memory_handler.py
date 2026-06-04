from personal_memory import remember_fact
from personal_memory import get_fact

def process_memory(query):

    q = query.lower()

    if "my name is" in q:

        name = query.split("is", 1)[1].strip()

        remember_fact("name", name)

        return f"I will remember your name is {name}"

    if "what is my name" in q:

        name = get_fact("name")

        if name:
            return f"Your name is {name}"

        return "I don't know your name yet."

    return None