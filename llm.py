import ollama

from memory import load_memory
from memory import save_memory

chat_history = load_memory()

def ask_ai(prompt):

    global chat_history

    chat_history.append({
        "role": "user",
        "content": prompt
    })

    recent_history = chat_history[-10:]   # keep only last 10 messages

    response = ollama.chat(
        model="gemma3:1b",
        messages=recent_history
    )

    answer = response["message"]["content"]

    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    save_memory(chat_history)

    return answer