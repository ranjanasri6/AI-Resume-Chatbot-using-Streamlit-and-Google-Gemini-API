import streamlit as st
import PyPDF2
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("💬 My Own Resume Chatbot")

# -------- PDF Reader --------
def get_resume_text(pdf):
    reader = PyPDF2.PdfReader(pdf)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


# -------- Upload Resume --------
pdf = st.file_uploader("Upload Resume", type=["pdf"])

if pdf:
    resume = get_resume_text(pdf)
    st.success("Resume loaded successfully!")

    # Chat input
    question = st.text_input("Ask something about my resume:")

    if question:

        prompt = f"""
You are my personal resume chatbot.

RULES:
- Answer ONLY using the resume.
- If the answer is not available, reply:
  "Not available in resume."
- Do not guess.

RESUME:
{resume}

QUESTION:
{question}
"""

        response = model.generate_content(prompt)

        st.write("🤖 Bot:")
        st.write(response.text)