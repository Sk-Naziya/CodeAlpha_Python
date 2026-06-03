import streamlit as st
from pypdf import PdfReader
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("📄 Knowledge Files")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text() + "\n"

    st.success("PDF Loaded Successfully")

    question = st.text_input(
        "Ask a question about the PDF"
    )

    if st.button("Ask AI"):

        with st.spinner("Analyzing PDF..."):

            prompt = f"""
            PDF Content:

            {text[:12000]}

            User Question:

            {question}

            Answer using only the PDF content.
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response.choices[0].message.content

            st.subheader("Answer")

            st.write(answer)