import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
from google.genai import types

# this loads the env of the token
load_dotenv()

# starting of FLask app
app = Flask(__name__)
CORS(app)


api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) 

users_db = {
    "admin@tadashi.com": "admin123"
}

# 1. Create a chat session that stays open and remembers history
chat_session = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are TADASHI, a helpful AI assistant. "
            "Be polite and positve until not asked to be honest. "
            "You are made by SATYAM VISHWAKARMA. "
            "Your API is made by GOOGLE GEMINI. "
            "Always provide short, concise responses. "
            "Use simple language."
        ),
        temperature=0.7
    )
)

# Reset chat
@app.route('/reset', methods=['POST'])
def reset_chat():
    global chat_session
    # Overwrite the old session with a fresh one
    chat_session = client.chats.create(
        model='gemini-2.5-flash',
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are TADASHI, a helpful AI assistant. "
                "Be polite and positve until not asked to be honest. "
                "You are made by SATYAM VISHWAKARMA. "
                "Your API is made by GOOGLE GEMINI. "
                "Always provide short, concise responses. "
                "Use simple language."
            ),
            temperature=0.7
        )
    )
    # returns success if reset
    return jsonify({"status": "success"})

# Login
@app.route('/login', methods=['POST'])
def login():
    # ... keep your existing login code exactly the same ...
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in users_db and users_db[email] == password:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Incorrect Email or Password"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    try:
        # 2. Use send_message() on the chat session instead of creating new content
        response = chat_session.send_message(user_message)
        # returns the response
        return jsonify({"reply": response.text})
    except Exception as e:
        # returns error if API fails
        return jsonify({"reply": f"API Error: {str(e)}"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=False)