from llm import ask_ai

def ask_notes(question, context_chunks):

    context = "\n\n".join(context_chunks)

    prompt = f"""
Answer the question using only the provided notes.

Notes:
{context}

Question:
{question}
"""

    return ask_ai(prompt)