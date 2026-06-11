from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text

text = load_pdf("documents/os_notes.pdf")

chunks = chunk_text(text)

print("Total Chunks:", len(chunks))
print("\nFirst Chunk:\n")
print(chunks[0])