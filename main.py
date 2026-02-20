from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

clint = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = input("Enter the prompt -> ")
resource = clint.models.generate_content(model="gemini-2.5-flash", contents=prompt)


print("TADASHI -> " + resource.text)
