from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import get_embeddings
from rag.vector_store import create_index
from rag.retriever import retrieve
from rag.rag_chat import ask_notes

text = load_pdf("documents/OS_Notes.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

index = create_index(embeddings)

question = "What is deadlock?"

relevant_chunks = retrieve(
    question,
    index,
    chunks
)

answer = ask_notes(
    question,
    relevant_chunks
)

print(answer)