from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import get_embeddings
from rag.vector_store import create_index

text = load_pdf("documents/os_notes.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

index = create_index(embeddings)

print(index.ntotal)