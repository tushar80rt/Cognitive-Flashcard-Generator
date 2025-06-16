# 🧠 Cognitive Flashcard Generator

A Streamlit-powered AI application that generates intelligent flashcards from uploaded PDFs using the Mistral language model. Designed for students, educators, and lifelong learners to quickly revise and retain key concepts.

![Streamlit App Screenshot](<img width="959" alt="front page ai intern" src="https://github.com/user-attachments/assets/d7ef5f11-444d-4860-877c-ca521d7eb05b" />
)

## 📽️ Demo

[![Watch the demo](https://youtu.be/3vt604koQxw?si=j1Clj8uJ-0tSK6U_)

---

## 🚀 Features

- 📄 Upload academic PDFs (notes, textbooks, etc.)
- 🤖 Auto-generate question-answer flashcards using Mistral AI
- 🧠 Extracts key concepts intelligently
- 🔍 Easy-to-use Streamlit interface
- 💾 Save and reuse flashcards

---

## 🛠️ Tech Stack

| Technology      | Description                           |
|------------------|---------------------------------------|
| Python           | Core programming language             |
| Streamlit        | Frontend framework                    |
| Mistralai SDK    | Mistral AI LLM API                    |
| pdf2image        | Convert PDF pages to images           |
| pytesseract      | OCR to extract text from images       |
| dotenv           | For managing API keys securely        |

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tushar80rt/Cognitive-Flashcard-Generator.git
   cd Cognitive-Flashcard-Generator

2. Create a virtual environment (recommended)
     python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4.Set up environment variables

Create a .env file in the root directory
  Add your Mistral API key:
     MISTRAL_API_KEY=your_api_key_here

5. Run the app
    streamlit run app.py

6.📸 How It Works
 Upload a PDF (e.g., class notes).

 App extracts text via OCR (pdf2image + pytesseract).

 Mistral LLM generates flashcards from the content.

 View, save, or practice flashcards in the Streamlit interface.

7.🧑‍💻 Author

Tushar Singh

📧 [tushar80rt@gmail.com]

https://www.linkedin.com/in/tushar-singh-1ba975296/[linkdin]




