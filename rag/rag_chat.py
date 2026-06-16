from llm import ask_ai

def review_projects(context_chunks):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a senior software engineer and technical interviewer.

Review the following projects.

For each project provide:

1. Strengths
2. Weaknesses
3. Technologies used
4. Resume improvements
5. Interview questions that may be asked

Projects:
{context}

Provide detailed feedback.
"""

    return ask_ai(prompt)

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