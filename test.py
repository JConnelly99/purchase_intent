import pandas as pd
from functions import query_chatgpt, get_embedding, semantic_similarity
import matplotlib.pyplot as plt

# Read in the Excel file
file_path = 'data/Sally_Beauty_Customer_Personas.xlsx'  # Replace 'your_file.xlsx' with the actual file name
data = pd.read_excel(file_path)

# Define anchors for Likert scoring
anchors = {
    "1": "Strongly disagree",
    "2": "Disagree",
    "3": "Neutral",
    "4": "Agree",
    "5": "Strongly agree"
}

# Initialize columns for storing results
data['Likert_Probabilities'] = None
data['Max_Score_Key'] = None

model = "gpt-5-mini"

instructions = """
            You are participating in a consumer product survey. 
            You will impersonate a consumer with specific demographic attributes. 
            Answer as if you are that person, responding naturally and briefly to the question about your purchase intent.
            Do not give a number or Likert rating.
            """

# Get User Input for each Persona
for index, persona in enumerate(data['Persona']):
    product_description = "AURAFOAM™ is a body wash infused with mood-coded fragrances for relaxation or energy."  # Replace with actual product description
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

    # Store results in the DataFrame
    data.at[index, 'Likert_Probabilities'] = str(likert_probs)  # Convert dict to string for storage
    max_score_key = max(likert_probs, key=likert_probs.get)
    data.at[index, 'Max_Score_Key'] = max_score_key

    # Display results
    print("LLM Response:")
    print(response)

    print("Likert Probabilities:")
    print(likert_probs)

    print(f"The Likert Score for this user is: {max_score_key}")

print(data[['Persona', 'Likert_Probabilities', 'Max_Score_Key']])

import matplotlib.pyplot as plt

# Create a histogram of the Max_Score_Key
plt.figure(figsize=(10, 6))
data['Max_Score_Key'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Histogram of Max Score Key')
plt.xlabel('Likert Score')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
