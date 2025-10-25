import streamlit as st
from functions import query_chatgpt, get_embedding, semantic_similarity

# Define anchors for Likert scoring
anchors = {
    "1": "Strongly disagree",
    "2": "Disagree",
    "3": "Neutral",
    "4": "Agree",
    "5": "Strongly agree"
}

#persona = "35-year-old woman, moderate income, urban area, enjoys skincare and wellness routines."
#product_description = "AURAFOAM™ is a body wash infused with mood-coded fragrances for relaxation or energy."

# Streamlit app
st.title("LLM-Powered Likert Scoring App")

# User input
model = st.selectbox("Select Model", ["gpt-5-mini"])
instructions = """
            You are participating in a consumer product survey. 
            You will impersonate a consumer with specific demographic attributes. 
            Answer as if you are that person, responding naturally and briefly to the question about your purchase intent.
            Do not give a number or Likert rating.
            """
persona = st.text_input("Enter persona")
product_description = st.text_input("Enter your product description")

if st.button("Submit"):
    try:
        # Get User Input
        user_input = f"""
            Persona: {persona}
            Product Concept: {product_description}

            Question: How likely are you to purchase this product?
            Answer in one or two sentences.
            """
        # Query the LLM
        response = query_chatgpt(model, instructions, user_input)
        resp_emb = get_embedding(response)

        # Calculate Likert probabilities
        scores = {k: semantic_similarity(resp_emb, get_embedding(v)) for k, v in anchors.items()}
        min_score = min(scores.values())
        likert_probs = {k: round((v - min_score) / (sum(scores.values()) - len(scores) * min_score), 2) for k, v in scores.items()}

        # Display results
        st.subheader("LLM Response")
        st.write(response)

        st.subheader("Likert Probabilities")
        st.write(likert_probs)

        max_score_key = max(likert_probs, key=likert_probs.get)
        st.success(f"The Likert Score for this user is: {max_score_key}")

    except Exception as e:
        st.error(f"Error: {e}")