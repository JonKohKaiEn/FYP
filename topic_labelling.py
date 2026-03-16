import pandas as pd

csv_file = "question_bank.csv"

# load the CSV into a pandas DataFrame
print(f"Loading {csv_file}...")
df = pd.read_csv(csv_file)

total_questions = len(df)
print(f"Loaded {total_questions} questions.\n")
print("Type your topics separated by commas (e.g., 'limits, continuity').")
print("Type 'quit' at any time to save and exit.\n")

# loop through each question in the DataFrame
for index, row in df.iterrows():
    if pd.notna(row["topics"]) and str(row["topics"]).strip() != "":
        continue

    print("-" * 50)
    print(
        f"Question {index + 1} of {total_questions} (Major Topic: {row['major_topic']})"
    )
    print(f"Question: {row['question']}\n")

    user_input = input("Enter topics for this question (q to quit and save): ")

    if user_input.strip().lower() == "q":
        print("\nSaving progress and exiting...")
        break

    df.at[index, "topics"] = user_input.strip()

# Save the updated DataFrame back to a CSV file
output_file = "question_bank.csv"
df.to_csv(output_file, index=False)
print(f"\nDone! Updated questions saved to {output_file}")
