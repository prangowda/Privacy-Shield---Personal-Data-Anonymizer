# Privacy-Shield--Personal-Data-Anonymizer
This Python tool anonymizes sensitive personal data in CSV or text files. It helps protect privacy by masking names, emails, phone numbers, credit card details, and addresses while maintaining the file structure. This is useful for data sharing, analytics, and compliance with privacy laws like GDPR and CCPA.

🛠 Features:

  ✅ Automatically detects and anonymizes personal data (Names, Emails, Phone Numbers, etc.).

  ✅ Supports CSV and Text Files for easy integration.

  ✅ Customizable Masking (Replace with XXXX, random names, or hashed values).

  ✅ Fast & Efficient using pandas and re (regex).

  ✅ Data Privacy Protection for secure data sharing.

📜 Step 1: Install Dependencies

    pip install pandas faker
    
 🔹  pandas – Handles CSV files.

 🔹 faker – Generates fake but realistic replacement data.

📂 Step 2: Python Code (privacy_shield.py)

📂 Step 3: How to Use

   1. Run the Python script

          python privacy_shield.py
      
  2. Enter file type (csv or text).
     
  3.  Enter file path (e.g., data.csv or sample.txt).
    
  5.  Anonymized file is saved as anonymized_data.csv or anonymized_text.txt.







