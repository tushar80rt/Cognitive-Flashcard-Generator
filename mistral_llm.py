from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv("api.env")

api_key = os.getenv("MISTRAL_API_KEY")

def generate_flashcards(text, subject="General"):
    prompt = f"""
You are an expert teacher in {subject}. Read the content below and generate 10–15 Q&A flashcards. Each flashcard should have:
- A concise question
- A factual and self-contained answer

Content:
{text}
"""
    with Mistral(api_key=api_key) as mistral:
        response = mistral.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
