import time
import streamlit as st
import chromadb
import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

# Initialize ChromaDB
CHROMA_PATH = r"VECTOR DATABASE"
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="psychologist")

# Configure Gemini API
genai.configure(api_key=os.getenv("Google_API_KEY"))

def get_chat_response(user_query, chat_history):
    results = collection.query(query_texts=[user_query], n_results=1)
    history_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])

    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        system_instruction=f"""
        You are a compassionate and deeply empathetic psychologist. Your goal is to provide a safe space where the user feels heard, understood, and supported.
        Respond in a warm and non-judgmental manner, offering emotional validation and gentle guidance.

        Always prioritize active listening, use open-ended questions to encourage reflection, and offer comfort when needed.
        If relevant, provide simple mindfulness or grounding techniques to help the user feel more at ease.

        Strictly answer ONLY based on the provided context and conversation history.
        Context: {results['documents']}
        Conversation History: {history_text}
        """
    )

    response = model.generate_content(user_query)
    return response.text

# Streamlit UI
st.set_page_config(page_title="❤️ AI Psychologist", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .assistant-message {
            text-align: left !important;
            background: linear-gradient(90deg, #590d22, #800f2f, #a4133c, #c9184a, #ff4d6d, #ff758f);
            color: white;
            padding: 12px;
            border-radius: 20px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
        }
        .user-message {
            text-align: right !important;
            background-color: #333333;
            color: white;
            padding: 12px;
            border-radius: 20px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
            margin-left: auto !important;
        }
        .typing {
            font-style: italic;
            color: gray;
            padding: 10px;
            margin: 5px 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>AI Psychologist Chat ❤️</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to render messages properly
def render_message(content):
    code_block_pattern = r'```(python|json)(.*?)```'
    parts = re.split(code_block_pattern, content, flags=re.DOTALL)

    for i in range(0, len(parts), 3):
        text_part = parts[i].strip()
        if text_part:
            st.markdown(f'<div class="assistant-message">{text_part}</div>', unsafe_allow_html=True)

        if i + 1 < len(parts):
            language = parts[i + 1]
            code_part = parts[i + 2].strip()
            if code_part:
                st.code(code_part, language=language)

# Display past chat messages
for message in st.session_state.messages:
    if message["role"] == "assistant":
        render_message(message["content"])
    else:
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)

# User input field
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

    # Typing animation placeholder
    typing_placeholder = st.empty()
    typing_placeholder.markdown('<div class="typing">Typing...</div>', unsafe_allow_html=True)
    time.sleep(1)  # Pause before showing response

    # Get AI response
    response_text = get_chat_response(user_input, st.session_state.messages)
    
    # Remove typing animation and show response with incremental typing effect
    typing_placeholder.empty()
    response_container = st.empty()
    partial_response = ""

    for word in response_text.split():
        partial_response += word + " "
        response_container.markdown(f'<div class="assistant-message">{partial_response}</div>', unsafe_allow_html=True)
        time.sleep(0.05)  # Simulates typing effect

    st.session_state.messages.append({"role": "assistant", "content": response_text})
    render_message(response_text)

    st.rerun()
