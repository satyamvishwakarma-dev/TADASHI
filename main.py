import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
from google.genai import types # Import types for configuration

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) 

users_db = {
    "admin@tadashi.com": "password123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in users_db and users_db[email] == password:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Invalid email or password."})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    try:
        # Add system configurations here
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are TADASHI, a helpful AI assistant. made by Satyam Vishwakarma"
                    "your name means The Thinking, Articulating, Decision-making, Adaptive, Self-learning, Heuristic, Intelligent System in short TADASHI"

                ),
                temperature=0.7 # Optional: Controls how creative the bot is (0.0 to 2.0)
            )
        )
        
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"API Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)