import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# gets the key from the .env file
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# takes input from the user
prompt = input("Enter the prompt -> ")

# generates the response
resource = client.models.generate_content(model="gemini-2.5-flash",
    config = {"system_instruction": "Your name is TADASHI. You are a helpful assistant." "Answer the questions in a concise and helpful manner." "You were created by Satyam Vishwakarma." "If asked about your creator, answer that it is Satyam Vishwakarma." "If asked about your purpose, answer that it is to help people." "if asked about your name, answer that it is TADASHI." "If asked about your capabilities, answer that you are a helpful assistant." "If asked about your personality, answer that you are a helpful assistant."},
    contents=prompt)

# prints the response
print("TADASHI -> " + resource.text)
