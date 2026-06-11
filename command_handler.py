from memory_handler import process_memory
from commands import execute_command
from rag.rag_engine import ask_pdf
from llm import ask_ai

def handle_command(command):

    # Memory
    memory_response = process_memory(command)

    if memory_response:
        return memory_response

    # System Commands
    result = execute_command(command)

    if result:
        return result

    # PDF Questions
    if command.lower().startswith("notes"):

        question = command[5:].strip()

        return ask_pdf(question)

    # Default AI
    return ask_ai(command)