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
resource = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

# prints the response
print("TADASHI -> " + resource.text)
