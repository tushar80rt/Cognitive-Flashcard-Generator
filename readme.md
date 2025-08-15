# 🧠 Cognitive Flashcard Generator

Generate study-ready Q&A flashcards from PDFs using a Streamlit app powered by the Mistral LLM.

---

## ✅ Quickstart

```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Configure API key (the app reads api.env)
# Replace YOUR_API_KEY with your actual Mistral API key
printf "MISTRAL_API_KEY=YOUR_API_KEY\n" > api.env

# 4) Run the app
streamlit run app.py
```

Then open the provided local URL in your browser.

---

## ⚙️ What this app does
- Upload a text-based PDF (notes, handouts, chapters)
- Choose a subject area to guide generation
- Generate 10–15 concise Q&A flashcards with factual, self-contained answers
- Download results as TXT or CSV

---

## 📂 Project structure
- `app.py`: Streamlit UI and interaction flow
- `mistral_llm.py`: Mistral client and flashcard generation logic (reads `MISTRAL_API_KEY` from `api.env`)
- `utils.py`: PDF text extraction using `PyPDF2`
- `requirements.txt`: Python dependencies

---

## 🔐 Configuration
- Create a file named `api.env` in the project root with:
  ```
  MISTRAL_API_KEY=YOUR_API_KEY
  ```
- The key is loaded via `python-dotenv` in `mistral_llm.py`:
  ```python
  load_dotenv("api.env")
  ```

---

## 🛠️ Requirements
- Python 3.9+
- Internet access for Mistral API calls
- Packages from `requirements.txt`:
  - `streamlit`, `mistralai`, `python-dotenv`, `PyPDF2`

---

## 🧪 Usage tips
1. Use text-based PDFs. Scanned PDFs (images) are not supported in this version.
2. Large PDFs may take longer to process; consider splitting long documents.
3. Choose the most relevant subject for better results.

---

## ❗ Troubleshooting
- "No API key" or authentication errors:
  - Ensure `api.env` exists and contains `MISTRAL_API_KEY=...`
  - Restart the app after changes
- Empty or garbled text:
  - Your PDF may be image-only; this app currently parses text-only PDFs
- Rate limit or network errors:
  - Retry after a short delay; ensure stable internet connectivity

---

## 📝 License
Add your preferred license here (e.g., MIT) if distributing.