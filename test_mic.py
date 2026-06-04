from llm import ask_ai
from speech import listen

while True:
    text = listen()
    print("Detected:", text)