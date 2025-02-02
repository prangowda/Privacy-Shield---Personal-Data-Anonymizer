import pandas as pd
import re
from faker import Faker

fake = Faker()

# Regular expressions for detecting sensitive data
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
CREDIT_CARD_REGEX = r"\b\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}\b"

# Function to anonymize text
def anonymize_text(text):
    if re.match(EMAIL_REGEX, text):
        return fake.email()
    elif re.match(PHONE_REGEX, text):
        return fake.phone_number()
    elif re.match(CREDIT_CARD_REGEX, text):
        return "XXXX-XXXX-XXXX-XXXX"
    elif text.replace(" ", "").isalpha():
        return fake.name()  # Replace names
    return text

# Process CSV file
def anonymize_csv(file_path, output_path="anonymized_data.csv"):
    df = pd.read_csv(file_path)
    
    # Anonymize all columns
    for col in df.columns:
        df[col] = df[col].astype(str).apply(anonymize_text)
    
    df.to_csv(output_path, index=False)
    print(f"✅ Anonymized data saved to: {output_path}")

# Process Text file
def anonymize_text_file(file_path, output_path="anonymized_text.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    anonymized_text = re.sub(EMAIL_REGEX, fake.email(), text)
    anonymized_text = re.sub(PHONE_REGEX, fake.phone_number(), anonymized_text)
    anonymized_text = re.sub(CREDIT_CARD_REGEX, "XXXX-XXXX-XXXX-XXXX", anonymized_text)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(anonymized_text)
    
    print(f"✅ Anonymized text saved to: {output_path}")

# Run anonymization
if __name__ == "__main__":
    file_type = input("Enter file type (csv/text): ").strip().lower()
    file_path = input("Enter file path: ").strip()

    if file_type == "csv":
        anonymize_csv(file_path)
    elif file_type == "text":
        anonymize_text_file(file_path)
    else:
        print("❌ Invalid file type! Use 'csv' or 'text'.")
