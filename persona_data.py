import pandas as pd

# Define persona data with demographic details
personas = [
    {
        "Persona": """
        A 29-year-old independent hairstylist who runs a small home salon 
        and regularly shops at Sally Beauty for professional-grade bleach, 
        toners, and hair color. Shes interested in products that provide consistent results,
        help her manage multiple client hair types, and fit within her limited back-bar budget.
        She values Sallys loyalty program and often watches educational videos about new coloring techniques.
        """,
        "Gender": "Female",
        "Income Level": "Middle income ($45K–$70K)",
        "Marital Status": "Single",
        "Age Bracket": "25–34",
        "Ethnicity": "Hispanic"
    },
    {
        "Persona": """
        A 41-year-old office manager who colors her roots at home every six weeks
         to save on salon costs. She’s looking for reliable, easy-to-use permanent 
         hair color and developer that doesn’t damage her hair. She follows online 
         tutorials and wants to understand how to tone brassiness and select the 
         right shade from Sally’s range of professional color brands.
        """,
        "Gender": "Female",
        "Income Level": "Middle income ($55K–$80K)",
        "Marital Status": "Married",
        "Age Bracket": "35–44",
        "Ethnicity": "White"
    },
    {
        "Persona": """
        A 22-year-old college student experimenting with bold hair colors
         and nail designs as a form of self-expression. She shops at Sally
          Beauty for temporary dyes, bright nail polishes, and affordable
           styling tools. She often looks for cruelty-free and vegan
            options and follows Sally on TikTok for creative ideas and discount alerts.
        """,
        "Gender": "Female",
        "Income Level": "Low income (<$35K)",
        "Marital Status": "Single",
        "Age Bracket": "18–24",
        "Ethnicity": "White"
    },
    {
        "Persona": """
        A 33-year-old licensed nail technician who operates a small studio
         and buys all her gel polishes, acrylic powders, and sanitation 
         supplies in bulk from Sally. She values professional-grade 
         consistency and clear labeling on product ingredients. She’s 
         particularly interested in new UV/LED systems and how to extend 
         the life of client manicures.
        """,
        "Gender": "Female",
        "Income Level": "Middle income ($50K–$75K)",
        "Marital Status": "Single",
        "Age Bracket": "25–34",
        "Ethnicity": "Black"
    },
    {
        "Persona": """
        A 48-year-old salon owner managing a team of stylists who rely 
        on her for inventory management. She uses Sally Beauty as a primary 
        supplier for hair color, developer, and tools. Her focus is on building 
        a predictable ordering schedule, accessing business discounts, and 
        staying updated on discontinued or reformulated products that could 
        impact her stylists’ workflows.
        """,
        "Gender": "Female",
        "Income Level": "Upper-middle income ($70K–$100K)",
        "Marital Status": "Married",
        "Age Bracket": "45–54",
        "Ethnicity": "White"
    },
    {
        "Persona": """
        A 26-year-old barber who prides himself on clean fades and sharp lineups. 
        He visits Sally for clippers, guards, and disinfectants. 
        He’s interested in learning the technical differences between 
        clipper motors and blade metals, and how to properly maintain them 
        for long-term use in a high-volume shop.
        """,
        "Gender": "Male",
        "Income Level": "Middle income ($45K–$65K)",
        "Marital Status": "Single",
        "Age Bracket": "25–34",
        "Ethnicity": "Hispanic"
    },
    {
        "Persona": """
        A 56-year-old retiree who enjoys maintaining her hair at home and 
        experimenting with toners to embrace her gray rather than cover it. 
        She appreciates guidance from in-store associates on which silver 
        shampoos prevent yellowing and is curious about treatments that add 
        shine and smoothness without harsh chemicals.
        """,
        "Gender": "Female",
        "Income Level": "Middle income ($40K–$60K, retirement)",
        "Marital Status": "Married",
        "Age Bracket": "55–64",
        "Ethnicity": "White"
    },
    {
        "Persona": """
        A 32-year-old esthetician who recently expanded her menu to 
        include brow tinting and facial waxing. She shops at Sally 
        for wax pots, strips, and soothing post-wax products. 
        She’s particularly interested in the technical properties of 
        hard wax vs. soft wax and how temperature affects results on different skin types.
        """,
        "Gender": "Female",
        "Income Level": "Middle income ($45K–$65K)",
        "Marital Status": "Single",
        "Age Bracket": "25–34",
        "Ethnicity": "Asian"
    },
    {
        "Persona": """
        A 24-year-old aspiring beauty influencer who uses Sally Beauty 
        products to create content for Instagram and YouTube. She focuses 
        on accessible, drugstore-level products that mimic high-end results. 
        She’s interested in how different lighting affects the appearance of 
        makeup and hair color on camera, and she values product consistency 
        for accurate reviews.
        """,
        "Gender": "Female",
        "Income Level": "Low to middle income ($30K–$55K)",
        "Marital Status": "Single",
        "Age Bracket": "18–24",
        "Ethnicity": "White"
    },
    {
        "Persona": """
        A 38-year-old single father who cuts his kids’ hair at home to save money. 
        He relies on Sally Beauty for clippers, combs, and cape accessories. 
        He’s interested in tutorials on blending and trimming techniques and 
        wants durable, easy-to-clean equipment that helps him achieve a 
        professional look without formal training.
        """,
        "Gender": "Male",
        "Income Level": "Middle income ($40K–$60K)",
        "Marital Status": "Single",
        "Age Bracket": "35–44",
        "Ethnicity": "Hispanic"
    }
]

# Create DataFrame
df = pd.DataFrame(personas)

# Save as Excel file
file_path = "data/Sally_Beauty_Customer_Personas.xlsx"
df.to_excel(file_path, index=False)
