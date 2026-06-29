# 🤖 AI Resume Chatbot

An intelligent Resume Chatbot built using **Python**, **Streamlit**, and **Google Gemini API**. The application allows users to upload their resume in PDF format and ask questions about their qualifications, skills, education, projects, certifications, and experience. The chatbot responds only using the information available in the uploaded resume.

---

## 🚀 Features

- 📄 Upload resume in PDF format
- 🤖 AI-powered chatbot using Google Gemini API
- 💬 Ask questions about your resume
- ✅ Answers are generated only from the uploaded resume
- 🚫 Prevents hallucinations by replying "Not available in resume" when information is missing
- 🎨 Simple and user-friendly Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-dotenv

---

## 📂 Project Structure

```
ResumeChatbot/
│── app.py
│── .env
│── .gitignore
│── requirements.txt
│── README.md
```

> **Note:** The `.env` file is excluded from GitHub because it contains your API key.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/resume-chatbot.git
```

### 2. Move into the project folder

```bash
cd resume-chatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Questions

- Tell me about yourself.
- What are my technical skills?
- What projects have I completed?
- What programming languages do I know?
- What certifications do I have?
- What is my educational background?
- What internships have I completed?
- What are my strengths?

---

## 📸 Application Workflow

1. Upload your resume (PDF).
2. Enter a question about the resume.
3. The chatbot analyzes the uploaded resume.
4. Gemini AI generates an answer based only on the resume.
5. If the information is unavailable, the chatbot responds:
   > **"Not available in resume."**

---

## 🔒 Security

- API keys are stored securely using a `.env` file.
- Sensitive files are excluded using `.gitignore`.
- The chatbot does not use external information beyond the uploaded resume.

---

## 📜 License

This project is developed for educational and learning purposes.

---

## 👩‍💻 Author

**Ranjana**

Built using Python, Streamlit, and Google Gemini API.