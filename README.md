# ❤️ AI Psychologist Chatbot (Windows Edition)

Welcome to the AI Psychologist Chatbot, a safe space for you to explore your thoughts and feelings. This project leverages the power of Large Language Models (LLMs) and vector databases to provide empathetic and supportive conversations. Think of it as a digital companion, ready to listen and offer gentle guidance. This README is specifically tailored for Windows users.

## 🚀 Getting Started

### Prerequisites

Before you dive in, make sure you have the following installed:

*   Python 3.7+ (Recommended: Install from [python.org](https://www.python.org/downloads/windows/)) *Make sure to check the "Add Python to PATH" option during installation.*
*   A Google Cloud Project with the Vertex AI API enabled. You'll need an API key for [Gemini](https://aistudio.google.com/apikey).

### Installation

1.  Clone this repository:

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv .venv
    .venv\Scripts\activate 
    ```

3.  Install the dependencies using `pip` and your `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up your environment variables:

    *   Create a `.env` file in the root directory.
    *   Add your Google API key from [website](https://aistudio.google.com/apikey) :

        ```.env
        Google_API_KEY=YOUR_ACTUAL_API_KEY
        ```

### Running the App 

1.  Activate the virtual environment (if you haven't already): 
    ```bash
    .venv\Scripts\activate
    ```

2.  Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

    This will open the chatbot in your default web browser.

## 🛠️ How it Works 
1.  **Streamlit:**  Handles the user interface and interaction.
2.  **ChromaDB:** Stores and retrieves relevant context based on user input.
3.  **Gemini (LLM):**  Powers the chatbot's responses, generating empathetic and contextually appropriate text.
4.  **.env and `python-dotenv`:** Manages sensitive information like API keys securely.
![image](https://github.com/user-attachments/assets/b9057e09-104e-4d63-8e2b-c4e9df4302e1)

## 📄 License 
MIT License

## 🙏 Acknowledgements 
*   This project uses the powerful Gemini API from Google.
*   Thanks to the developers of Streamlit and ChromaDB.
