from src.config import GOOGLE_API_KEY
from google import genai

def query_db(db, embed_fn, query_text, n_results=1):
    # Switch to query mode when generating embeddings.
    embed_fn.document_mode = False

    result = db.query(query_texts=[query_text], n_results=n_results)
    return result["documents"][0]

def generate_answer(query_text, relevant_passages):
    client = genai.Client(api_key=GOOGLE_API_KEY)
    
    query_oneline = query_text.replace("\n", " ")

    # This prompt is where you can specify any guidance on tone, or what topics the model should stick to, or avoid.
    prompt = f"""You are a helpful and informative bot that answers questions using text from the reference passage included below. 
Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. 
However, you are talking to a non-technical audience, so be sure to break down complicated concepts and 
strike a friendly and converstional tone. If the passage is irrelevant to the answer, you may ignore it.

QUESTION: {query_oneline}
"""

    # Add the retrieved documents to the prompt.
    for passage in relevant_passages:
        passage_oneline = passage.replace("\n", " ")
        prompt += f"PASSAGE: {passage_oneline}\n"

    answer = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt)
        
    return answer.text
