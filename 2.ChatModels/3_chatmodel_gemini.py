import os

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
	raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file.")

# Use a broadly available Gemini chat model for compatibility.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

result = model.invoke("What is the capital of India?")

print(result.content)