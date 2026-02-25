import os
from google import genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

users_db = {
    "satyam@gmail.com": "123456"
}

@app.route("/login", methods = ["POST"])
def login():
    # Get the email and password from the request
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Check if the email and password are correct
    if email in users_db and users_db[email] == password:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid email or password"})

if __name__ == "__main__":
    app.run(debug=True)