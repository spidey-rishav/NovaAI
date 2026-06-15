from rag.model_loader import model

def get_embeddings(chunks):
    return model.encode(chunks)