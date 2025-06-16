import streamlit as st
from mistral_llm import generate_flashcards
from utils import extract_text_from_pdf

# Page Configuration
st.set_page_config(
    page_title="🧠 Flashcard Generator",
    layout="centered",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #1e1e1e;
            color: #f5f5f5;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            padding: 2rem;
        }
        h1, h2, h3, h4 {
            color: #66fcf1;
        }
        .stButton > button {
            background-color: #45a29e;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            border: none;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #2b7a78;
        }
        .flashcard-item {
            background-color: #2c2f33;
            border-left: 4px solid #45a29e;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 6px;
        }
        .stDownloadButton>button {
            background-color: #0b7285;
            color: white;
            border-radius: 6px;
            margin-top: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1>🧠 Cognitive Flashcard Generator</h1>", unsafe_allow_html=True)
st.markdown("Generate intelligent flashcards from your study materials using AI.")


with st.sidebar:
    st.markdown("## ⚙️ Settings")
    subject = st.selectbox(
        "**Subject Area**",
        ["General", "Life Sciences", "Physical Sciences", "Engineering", 
         "Humanities", "Business", "Medicine", "Law", "Information Technology"],
        index=0
    )
    st.markdown("---")
    st.markdown("📎 Upload a PDF file in the main area to begin.")


st.markdown("### 📄 Upload Your PDF")
uploaded_file = st.file_uploader("Upload learning materials", type=["pdf"])

if st.button("🚀 Generate Flashcards"):
    if uploaded_file:
        with st.spinner("Analyzing document and generating flashcards..."):
            try:
                content = extract_text_from_pdf(uploaded_file)
                flashcards = generate_flashcards(content, subject)

                st.success("✅ Flashcards generated successfully!")
                st.markdown("### 🧾 Your Flashcards")

                flashcard_list = [card for card in flashcards.split('\n') if card.strip()]
                for i, card in enumerate(flashcard_list, 1):
                    st.markdown(f'<div class="flashcard-item"><b>Card #{i}:</b> {card}</div>', unsafe_allow_html=True)

                # Downloads
                st.markdown("---")
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        "💾 Download as TXT",
                        data=flashcards,
                        file_name=f"flashcards_{subject}.txt",
                        mime="text/plain"
                    )
                with col2:
                    st.download_button(
                        "📥 Download as CSV",
                        data="\n".join([f"\"{card}\"" for card in flashcard_list]),
                        file_name=f"flashcards_{subject}.csv",
                        mime="text/csv"
                    )

            except Exception as e:
                st.error(f"⚠️ Generation failed: {str(e)}")
                st.markdown("""
                    <div style="background-color: #422727; padding: 1rem; border-radius: 6px;">
                        <p>📌 <strong>Troubleshooting Tips:</strong></p>
                        <ul>
                            <li>Make sure the PDF is not scanned</li>
                            <li>Try a smaller section of content</li>
                            <li>Ensure it's academic content</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("📤 Please upload a PDF to proceed.")





































