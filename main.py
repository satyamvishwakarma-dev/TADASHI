from google import genai
clint = genai.Client(api_key="AIzaSyCnpezmQduXKB0LsUHtrDDkZyROq4LnpS0")

prompt = input("Enter the prompt: ")
resource = clint.models.generate_content(model="gemini-2.5-flash", contents=prompt)


print("TADASHI -> " + resource.text)