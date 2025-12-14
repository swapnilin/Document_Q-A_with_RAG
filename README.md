# Gemini RAG Project

This project implements a Retrieval-Augmented Generation (RAG) system using Google's Gemini API and ChromaDB. It allows you to ask questions about a specific dataset (in this case, a manual for a "Googlecar").

## 🚀 How to Run

### Prerequisites
- Python 3.10+
- A Google Cloud API Key (for Gemini)

### Installation

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Setup**:
    - Create a file named `.env` in the project root:
      ```bash
      touch .env
      ```
    - Open `.env` and add your Google Cloud API key:
      ```
      GOOGLE_API_KEY=your_actual_api_key_here
      ```

### Usage

Run the main script with your question as a command-line argument:

```bash
python main.py "How do you use the touchscreen to play music?"
```

## 🧠 Code Flow

The application logic is modularized into several components within the `src/` directory. Here is the execution flow when you run `main.py`:

1.  **Initialization (`main.py`)**:
    - The script starts and parses the command-line argument (your question).
    - It calls `get_documents()` from `src/data.py` to load the raw text data.

2.  **Vector Database Setup (`src/vector_db.py` & `src/embeddings.py`)**:
    - `init_db()` is called to set up ChromaDB.
    - It uses `GeminiEmbeddingFunction` (from `src/embeddings.py`) which connects to the `text-embedding-004` model.
    - The documents are embedded (converted to vector representations) and stored in an in-memory ChromaDB collection.

3.  **Retrieval (`src/rag.py`)**:
    - `query_db()` takes your question and the database instance.
    - It converts your question into an embedding using the same model.
    - It performs a semantic search to find the most relevant document(s) in the database.

4.  **Generation (`src/rag.py`)**:
    - `generate_answer()` takes the retrieved passages and your original question.
    - It constructs a prompt that includes the context (retrieved passages) and instructions.
    - It sends this prompt to the `gemini-2.0-flash` model.
    - The model generates a natural language answer based on the provided context.

5.  **Output**:
    - The final answer is printed to the console.

## 📂 Project Structure

- `main.py`: Entry point for the CLI.
- `src/config.py`: Handles environment configuration.
- `src/data.py`: Stores the knowledge base (documents).
- `src/embeddings.py`: Wrapper for Gemini embeddings API.
- `src/vector_db.py`: Manages ChromaDB operations.
- `src/rag.py`: Core logic for retrieval and answer generation.
