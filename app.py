import streamlit as st
from functions import query_chatgpt, get_embedding, semantic_similarity
import pandas as pd
import matplotlib.pyplot as plt


# Read in the Excel file
file_path = 'data/Sally_Beauty_Customer_Personas.xlsx'  # Replace 'your_file.xlsx' with the actual file name
persona_data = pd.read_excel(file_path)

# Define anchors for Likert scoring
anchors = {
    1: "I definitely would not buy this product.",
    2: "I probably would not buy this product.",
    3: "I'm not sure if I would buy this product.",
    4: "I would probably buy this product.",
    5: "I definitely would buy this product."
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

product_description = st.text_input("Enter your product description")
persona = st.text_input("Enter persona")

if st.button("Run Analysis for Custom Persona Above"):
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

if st.button("Run Analysis for Multiple Personas"):
    try:
        # Get User Input for each Persona
        for index, persona in enumerate(persona_data['Persona']):
            #product_description = "AURAFOAM™ is a body wash infused with mood-coded fragrances for relaxation or energy."  # Replace with actual product description
            user_input = f"""
                Persona: {persona}
                Product Concept: {product_description}

                Question: How likely are you to purchase this product?
                Answer in one or two sentences.
                """
            #Print the persona   
            st.subheader("Persona")
            st.write(persona)

            # Query the LLM
            response = query_chatgpt(model, instructions, user_input)
            resp_emb = get_embedding(response)

            # Calculate Likert probabilities
            scores = {k: semantic_similarity(resp_emb, get_embedding(v)) for k, v in anchors.items()}
            min_score = min(scores.values())
            likert_probs = {k: round((v - min_score) / (sum(scores.values()) - len(scores) * min_score), 2) for k, v in scores.items()}

            # Store results in the DataFrame
            persona_data.at[index, 'Likert_Probabilities'] = str(likert_probs)  # Convert dict to string for storage
            max_score_key = max(likert_probs, key=likert_probs.get)
            persona_data.at[index, 'Max_Score_Key'] = max_score_key

            st.subheader("LLM Response")
            st.write(response)

            st.subheader("Likert Probabilities")
            st.write(likert_probs)

            #st.write("Raw similarity scores:", scores)
            #st.write("Response embedding:", resp_emb)

            print(f"The Likert Score for this user is: {max_score_key}")

        # Create a histogram of the Max_Score_Key
        st.title('Histogram of Max Score Key')
        
        # Create a Matplotlib figure
        fig, ax = plt.subplots()
        score_counts = persona_data['Max_Score_Key'].value_counts().sort_index()  # Count occurrences of each Max_Score_Key

        ax.bar(score_counts.index, score_counts.values, color='skyblue')
        ax.set_xlabel('Max Score Key')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Max Score Key')
        ax.set_xticks(score_counts.index)
        ax.set_xticklabels(score_counts.index, rotation=0)  # Keep x-axis labels horizontal

        # Display the chart in Streamlit
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
