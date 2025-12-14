import sys
from src.data import get_documents
from src.vector_db import init_db
from src.rag import query_db, generate_answer

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <question>")
        sys.exit(1)

    query = sys.argv[1]
    
    print("Initializing Database...")
    documents = get_documents()
    db, embed_fn = init_db(documents)
    
    print(f"Querying: {query}")
    relevant_passages = query_db(db, embed_fn, query)
    
    print("Generating Answer...")
    answer = generate_answer(query, relevant_passages)
    
    print("\n--- Answer ---")
    print(answer)

if __name__ == "__main__":
    main()
