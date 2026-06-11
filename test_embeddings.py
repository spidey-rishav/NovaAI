from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import get_embeddings

text = load_pdf("documents/os_notes.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

print(embeddings.shape)