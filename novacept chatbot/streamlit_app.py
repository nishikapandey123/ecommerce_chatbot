import streamlit as st
import requests

st.title("Novacept Chatbot Testing")

user_id = st.text_input("User ID")
question = st.text_area("Ask a question:")

if st.button("Submit"):
    response = requests.post(
        "http://localhost:5000/query",
        json={"user_id": user_id, "question": question}
    )
    st.write(response.json())
