import pandas as pd

csv_file = "question_bank.csv"

# load the CSV into a pandas DataFrame
print(f"Loading {csv_file}...")
df: pd.DataFrame = pd.read_csv(csv_file)
df["topics"] = df["topics"].fillna("").astype(str)

total_questions = len(df)
print(f"Loaded {total_questions} questions.\n")
print("Type your topics separated by commas (e.g., 'limits, continuity').")
print("Type 'q' at any time to save and exit.\n")

topic_list = {
    0: "Systems of Linear Equations and Matrices",
    1: "Gaussian Elimination",
    2: "Matrix Algebra",
    3: "Determinants",
    4: "Elementary Matrices",
    5: "LU Factorization",
    6: "Vector Spaces and Subspaces",
    7: "Linear Independence and Spanning Sets",
    8: "Basis and Dimension",
    9: "Rank and Nullity",
    10: "Eigenvalues and Eigenvectors",
    11: "Diagonalization",
    12: "Complex Numbers",
    13: "Euler's Formula and De Moivre's Formula",
    14: "Complex Logarithm and Powers",
    15: "Limits and Continuity of Complex Functions",
    16: "Differentiability and Analyticity of Complex Functions",
    17: "Cauchy-Riemann Equations",
    18: "Complex Integration",
    19: "Cauchy's Integral Theorem and Formula",
    20: "Vector Differentiation",
    21: "Scalar and Vector Fields",
    22: "Del Operator (Gradient, Divergence, and Curl)",
    23: "Directional Derivative",
    24: "Laplacian",
    25: "Vector Line Integrals",
    26: "Vector Surface Integrals",
    27: "Volume Integrals",
    28: "Conservative Vector Fields",
    29: "Scalar Triple Product",
}

# loop through each question in the DataFrame
for index, row in df.iterrows():
    if pd.notna(row["topics"]) and str(row["topics"]).strip() != "":
        continue

    print("-" * 50)
    print(
        f"Question {index + 1} of {total_questions} (Major Topic: {row['major_topic']})"
    )
    print(f"Question: {row['question']}\n")

    user_input = input(
        "Enter topic numbers for this question (q to quit and save): "
    ).strip()

    if user_input.lower() == "q":
        print("\nSaving progress and exiting...")
        quit_flag = True
        break

    else:
        topic_idxs = [int(i) for i in user_input.split()]
        input_topics = ",".join([topic_list[j] for j in topic_idxs])
        print(f"Selected topics: {input_topics}")
        df.at[index, "topics"] = input_topics

# Save the updated DataFrame back to a CSV file
output_file = "question_bank.csv"
df.to_csv(output_file, index=False)
print(f"\nDone! Updated questions saved to {output_file}")
