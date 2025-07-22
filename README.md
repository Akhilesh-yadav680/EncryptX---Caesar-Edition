# 🔐 Caesar Cipher Web App (Streamlit)

This project provides a simple and interactive Caesar Cipher tool to **encode or decode** messages using a shift value.

## 🚀 Features
- Clean Streamlit web interface
- Supports both **encryption** and **decryption**
- Handles special characters and spaces gracefully

## 📂 Files
EncryptX---Caesar-Edition/
│
├── .gitignore               # Git ignored files
├── LICENSE                  # MIT License
├── README.md                # Project description & usage
│
├── app.py                   # Streamlit UI for Caesar Cipher
├── caesar_ASCII_title.py    # Optional ASCII title art
├── ceaser_cipher.py         # Core Caesar Cipher logic
├── cli_cipher.py            # Optional CLI interface

## ▶️ How to Run
pip install -r requirements.txt
streamlit run app.py

🛠️ Built With
Python 🐍

Streamlit 🌐

✨ Example
Input: hello

Shift: 3

Output (Encode): khoor

🔒 What is Caesar Cipher?
A substitution cipher where each letter is shifted by a fixed number of positions in the alphabet.
