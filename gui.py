import customtkinter as ctk
from command_handler import handle_command
from speech import listen
from voice import speak
import threading

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Nova AI")
app.geometry("900x600")

chat_box = ctk.CTkTextbox(
    app,
    width=850,
    height=450
)
chat_box.pack(pady=20)


def add_message(message):

    chat_box.configure(state="normal")

    chat_box.insert("end", message)

    chat_box.configure(state="disabled")

    chat_box.see("end")


add_message(
    "Nova: Hello! I'm Nova. Ask me anything.\n\n"
)

def send_message():

    user_message = entry.get().strip()

    if not user_message:
        return

    send_btn.configure(state="disabled")

    add_message(f"You: {user_message}\n\n")

    entry.delete(0, "end")

    response = handle_command(user_message)

    add_message(f"Nova: {response}\n\n")

    send_btn.configure(state="normal")

def process_message(user_message):

    response = handle_command(user_message)

    add_message(f"Nova: {response}\n\n")

    send_btn.configure(state="normal")
    
entry = ctk.CTkEntry(
    app,
    width=700,
    placeholder_text="Ask Nova anything..."
)
entry.pack(pady=10)

def voice_chat():

    add_message("Listening...\n\n")

    command = listen()

    add_message(f"You (Voice): {command}\n\n")

    response = handle_command(command)

    add_message(f"Nova: {response}\n\n")

    speak(response)

send_btn = ctk.CTkButton(
    app,
    text="Send",
    command=send_message
)


send_btn.pack()

voice_btn = ctk.CTkButton(
    app,
    text="🎤 Speak",
    command=lambda: threading.Thread(
        target=voice_chat,
        daemon=True
    ).start()
)

voice_btn.pack(pady=10)

entry.bind(
    "<Return>",
    lambda event: send_message()
)

chat_box.configure(state="disabled")

app.mainloop()