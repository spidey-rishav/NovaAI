from memory_handler import process_memory
from commands import execute_command
from rag.rag_chat import review_projects
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
    
    project_keywords = [
        "review my project",
        "review my projects",
        "analyze my project",
        "analyse my project",
        "check my project"
    ]

    if any(keyword in command.lower() for keyword in project_keywords):
        return review_projects(command)

    # Default AI
    return ask_ai(command)
