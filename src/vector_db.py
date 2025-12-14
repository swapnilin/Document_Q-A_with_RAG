import chromadb
from src.embeddings import GeminiEmbeddingFunction

DB_NAME = "googlecardb"

def init_db(documents):
    embed_fn = GeminiEmbeddingFunction()
    embed_fn.document_mode = True

    chroma_client = chromadb.Client()
    db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)

    # Check if DB is empty to avoid re-adding documents if persisting (though here we use ephemeral client by default)
    if db.count() == 0:
        db.add(documents=documents, ids=[str(i) for i in range(len(documents))])
    
    return db, embed_fn
