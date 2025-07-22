# app.py

import streamlit as st
from ceaser_cipher import ceaser

st.set_page_config(page_title="Caesar Cipher", layout="centered")
st.title("🔐 Caesar Cipher - Encrypt & Decrypt")
st.markdown("This tool encodes or decodes messages using the Caesar cipher technique.")

option = st.radio("Choose Operation", ["Encode", "Decode"])
message = st.text_area("Enter your message", "")
shift = st.number_input("Enter Shift Number", min_value=1, max_value=25, step=1)

if st.button("Run Caesar Cipher"):
    if not message:
        st.warning("Please enter a message.")
    else:
        result = ceaser(message.lower(), shift, option.lower())
        st.success(f"**Result ({option}d):** `{result}`")
