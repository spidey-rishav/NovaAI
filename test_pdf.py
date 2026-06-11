from rag.pdf_loader import load_pdf

text = load_pdf("documents/os_notes.pdf")

print(text[:1000])