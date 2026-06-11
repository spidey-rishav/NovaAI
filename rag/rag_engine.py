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

def ask_pdf(question):

    context_chunks = retrieve(
        question,
        index,
        chunks
    )

    return ask_notes(
        question,
        context_chunks
    )