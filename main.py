from voice import speak
from speech import listen
from command_handler import handle_command


def voice_mode():

    print("\nVoice Chat Mode")

    WAKE_WORDS = ["nova", "hey nova"]

    while True:

        query = listen().lower()

        if any(word in query for word in WAKE_WORDS):

            speak("Yes?")

            command = listen()

            if command.lower() in [
                "exit",
                "quit",
                "back"
            ]:
                break

            response = handle_command(command)

            print("\nNova:", response)

            speak(response)


def text_mode():

    print("\nText Chat Mode")

    while True:

        command = input("You: ")

        if command.lower() in [
            "exit",
            "quit",
            "back"
        ]:
            break

        response = handle_command(command)

        print("\nNova:", response)

        speak(response)


while True:

    print("\n===== NOVA AI =====")
    print("1. Text Chat")
    print("2. Voice Chat")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        text_mode()

    elif choice == "2":
        voice_mode()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")