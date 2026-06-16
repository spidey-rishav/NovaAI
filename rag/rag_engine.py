import os
from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import get_embeddings
from rag.vector_store import create_index
from rag.retriever import retrieve
from rag.rag_chat import ask_notes
from rag.pdf_manager import load_all_pdfs

text = load_all_pdfs()

print("Text length:", len(text))

chunks = chunk_text(text)

print("Chunks:", len(chunks))

embeddings = get_embeddings(chunks)

print("Embeddings:", type(embeddings))
print("Embeddings shape:", embeddings.shape)

os.listdir("documents")

def ask_pdf(question):
    index = create_index(embeddings)
    context_chunks = retrieve(
        question,
        index,
        chunks
    )

    return ask_notes(
        question,
        context_chunks
    )