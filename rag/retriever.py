from rag.model_loader import model

def retrieve(query, index, chunks, k=10):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        query_embedding,
        k
    )

    return [chunks[i] for i in indices[0]]