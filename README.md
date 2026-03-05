# 🤖 TADASHI: Custom AI Assistant

![UI Showcase](https://img.shields.io/badge/UI-Glassmorphism-blue) ![Backend](https://img.shields.io/badge/Backend-Python%20Flask-brightgreen) ![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)

TADASHI is a sleek, custom-built AI chatbot designed to provide concise, helpful responses through a highly interactive and futuristic web interface. Powered by Google's latest Gemini 2.5 Flash model, it features contextual memory, secure environment configurations, and a seamless frontend-to-backend pipeline.

## ✨ Features

* **🧠 Context-Aware Memory**: TADASHI remembers the flow of the conversation using continuous chat sessions, allowing for natural, multi-turn interactions.
* **🌌 Futuristic UI**: A premium "Glassmorphism" design featuring a dynamic video background, glowing neon borders, and smooth CSS animations.
* **🔒 Secure Backend**: Built with Python and Flask, utilizing `.env` to keep API keys completely hidden from the frontend.
* **💬 Real-Time UX**: Includes animated bouncing-dot typing indicators and auto-scrolling for a natural chat feel.
* **🔄 One-Click Reset**: A dedicated "+ New Chat" function that instantly wipes the context window and resets the board.
* **🔐 Authentication**: A foundational login system routing users safely to the chat interface.

## 🛠️ Tech Stack

* **Frontend**: HTML5, CSS3 (Glassmorphism, Animations), Vanilla JavaScript (Fetch API)
* **Backend**: Python, Flask, Flask-CORS
* **AI Integration**: Google GenAI SDK (`google-genai`), Gemini 2.5 Flash Model
* **Environment Management**: `python-dotenv`

## 🚀 Getting Started

Follow these steps to run TADASHI on your local machine.

### Prerequisites
* Python 3.8+ installed on your system.
* A Google Gemini API key (Get one at [Google AI Studio](https://aistudio.google.com/)).

### Installation

1.  **Clone the repository**
    ```bash
    git clone 
    https://github.com/satyamvishwakarma-dev/TADASHI.git
    cd TADASHI
    ```

2.  **Install the required Python packages**
    ```bash
    pip install flask flask-cors python-dotenv google-genai
    ```

3.  **Set up your Environment Variables**
    Create a file named `.env` in the root directory and add your Gemini API key:
    ```text
    GEMINI_API_KEY=your_actual_api_key_here
    ```

4.  **Run the Flask Server**
    ```bash
    python main.py
    ```
    *The server will start running on `http://127.0.0.1:5000`*

5.  **Launch the App**
    Open `index.html` in your web browser. 
    * **Test Login Credentials (For this code only)**: 
        * **Email**: `admin@tadashi.com`
        * **Password**: `admin123`

## 📂 Project Structure

```text
TADASHI/
│
├── main.py             # Python Flask backend and API routing
├── .env                # Secret environment variables (DO NOT COMMIT)
├── .gitignore          # Tells Git to ignore .env and other cache files
│
├── index.html          # Login page structure
├── style.css           # Login page styling
├── script.js           # Login validation and redirect logic
│
├── chat.html           # Chatbot interface structure
├── chat.css            # Chatbot styling
└── chat.js             # Chatbot frontend logic and API fetching
```

## 👤 Author
### Satyam Vishwakarma
* GitHub: [satyamvishwakarma-dev](https://github.com/satyamvishwakarma-dev)
* LinkedIn: [satyamvishwakarma-cse](https://www.linkedin.com/in/satyamvishwakarma-cse/)
* X: [satyamv_dev](https://x.com/satyamv_dev)

## 📝TADASHI v2.0 (Under Development)
* Integrate SQLite or PostgreSQL to replace the dictionary-based login system.
* Implement persistent user sessions and save past chat logs to a database.
* Add Markdown parsing to the chat bubbles so TADASHI can output formatted code snippets.

