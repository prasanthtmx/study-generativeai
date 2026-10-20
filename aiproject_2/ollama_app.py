import os
from dotenv import load_dotenv
import ollama

load_dotenv()

ollama.configure(api_key=os.getenv("OLLAMA_API_KEY"))

model = "llama3.1:8b"

response = ollama.chat(model=model, messages=[{"role": "user", "content": "What is the capital of Paris?"}])

print(response)