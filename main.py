from llm import ask_ai
from commands import execute_command
from voice import speak
from speech import listen
from memory_handler import process_memory

while True:

    query = listen().lower()
    print("Heard:", query)

    if query == "exit":
        break

    WAKE_WORDS = ["nova", "hey nova"]

    while True:

        speak("Yes?")

        command = listen()

        # 1. Memory handling first
        memory_response = process_memory(command)

        if memory_response:
            print("Nova:", memory_response)
            speak(memory_response)
            continue

        # 2. System commands
        result = execute_command(command)

        if result:
            print("Nova:", result)
            speak(result)
            continue

        # 3. LLM fallback
        answer = ask_ai(command)

        print("Nova:", answer)
        speak(answer)

        continue