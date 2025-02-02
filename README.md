# Privacy Shield - Personal Data Anonymizer

## 🔍 Project Description
Privacy Shield is a **Python-based tool** designed to **anonymize personal data** in CSV or text files. It automatically detects and replaces sensitive information such as **names, emails, phone numbers, and credit card details**, ensuring data privacy and compliance with regulations like GDPR and CCPA.

---

## 🛠 Features
✅ Automatically detects and anonymizes **names, emails, phone numbers, and credit cards**  
✅ Supports **CSV and Text Files**  
✅ Customizable Masking (**Fake data, Hashing, or "XXXX" masking**)  
✅ Fast and efficient using **pandas** and **regex**  
✅ Helps in **data privacy protection** and **secure data sharing**  

---

## 📜 Installation
Install the required dependencies using pip:
```sh
pip install pandas faker
```

---

## 📂 Usage
Run the Python script:
```sh
python privacy_shield.py
```

Follow the prompts:
1. **Enter file type** (csv/text)
2. **Enter file path** (e.g., `data.csv` or `sample.txt`)
3. **Anonymized file is saved** as `anonymized_data.csv` or `anonymized_text.txt`

---

## 📊 Example Input & Output

### 🔹 **Original CSV (`data.csv`)**
| Name    | Email              | Phone       | Credit Card        |
|---------|--------------------|------------|---------------------|
| Alice   | alice@gmail.com    | 987-654-3210 | 1234-5678-9101-1121 |
| Bob     | bob@yahoo.com      | 876-543-2109 | 2345-6789-0123-4567 |

### 🔹 **Anonymized Output (`anonymized_data.csv`)**
| Name            | Email                  | Phone       | Credit Card        |
|----------------|------------------------|------------|---------------------|
| John Doe       | michael12@example.com  | 555-123-4567 | XXXX-XXXX-XXXX-XXXX |
| Sarah Smith    | anna.williams@mail.com | 333-987-6543 | XXXX-XXXX-XXXX-XXXX |

---

## 🚀 Future Enhancements
🔹 **Encrypt anonymized files** before sharing  
🔹 **Add database support** (MySQL/PostgreSQL)  
🔹 **Web-based UI for easy usage**  


