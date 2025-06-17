# 🧠 Cognitive Flashcard Generator

A Streamlit-powered AI application that generates intelligent flashcards from uploaded PDFs using the Mistral language model. Designed for students, educators, and lifelong learners to quickly revise and retain key concepts.

<img width="959" alt="intern first view" src="https://github.com/user-attachments/assets/c66f6e60-09f4-4c95-b068-05f49383561c" />

<img width="958" alt="Intern task second" src="https://github.com/user-attachments/assets/3f884fb1-6456-49a4-933f-6f1b5c972a16" />

<img width="959" alt="intern task third" src="https://github.com/user-attachments/assets/7c2eed60-ae38-4e1e-be70-39d90b460dee" />



## 📽️ Demo

https://youtu.be/3vt604koQxw?si=QpTjRW5aqHCgiRxt

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




