from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import get_embeddings
from rag.vector_store import create_index
from rag.retriever import retrieve

text = load_pdf("documents/OS_Notes.pdf")

chunks = chunk_text(text)

embeddings = get_embeddings(chunks)

index = create_index(embeddings)

results = retrieve(
    "What is deadlock?",
    index,
    chunks
)

for r in results:
    print("\n-----------------\n")
    print(r)