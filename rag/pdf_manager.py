import os
from rag.pdf_loader import load_pdf

def load_all_pdfs(folder="documents"):

    combined_text = ""

    for file in os.listdir(folder):

        if file.lower().endswith(".pdf"):

            path = os.path.join(folder, file)

            print(f"Loading {file}")

            combined_text += "\n\n" + load_pdf(path)

    return combined_text