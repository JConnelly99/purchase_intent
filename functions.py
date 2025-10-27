import numpy as np
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key is not set. Please set the 'OPENAI_API_KEY' environment variable.")

openai.api_key = st.secrets["openai"]["api_key"]

anchors = {
    1: "I definitely would not buy this product.",
    2: "I probably would not buy this product.",
    3: "I'm not sure if I would buy this product.",
    4: "I would probably buy this product.",
    5: "I definitely would buy this product."
}

def get_embedding(text):
    client = OpenAI(api_key=api_key)
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(resp.data[0].embedding)

def semantic_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def query_chatgpt(model, instructions, user_input):
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=user_input,
    )
    return response.output_text

# Example usage
if __name__ == "__main__":
    try:
        model = "gpt-5-mini"
        instructions = """
            You are participating in a consumer product survey. 
            You will impersonate a consumer with specific demographic attributes. 
            Answer as if you are that person, responding naturally and briefly to the question about your purchase intent.
            Do not give a number or Likert rating.
            """
        persona = "35-year-old woman, moderate income, urban area, enjoys skincare and wellness routines."
        product_description = "AURAFOAM™ is a body wash infused with mood-coded fragrances for relaxation or energy."

        user_input = f"""
            Persona: {persona}
            Product Concept: {product_description}

            Question: How likely are you to purchase this product?
            Answer in one or two sentences.
            """
        
        response = query_chatgpt(model, instructions, user_input)
        resp_emb = get_embedding(response)

        scores = {k: semantic_similarity(resp_emb, get_embedding(v)) for k, v in anchors.items()}

        # Normalize to a probability distribution
        min_score = min(scores.values())
        likert_probs = {k: round((v - min_score) / (sum(scores.values()) - len(scores) * min_score), 2) for k, v in scores.items()}

        print(response)
        print(likert_probs)

        max_score_key = max(likert_probs, key=likert_probs.get)
        print(f"The Likert Score for this user is: {max_score_key}")

    except Exception as e:
        print(f"Error: {e}")
