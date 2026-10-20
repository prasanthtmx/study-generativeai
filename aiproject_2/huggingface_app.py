import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

prompt = "What is the currency of India?"

client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_KEY"))

response = client.chat.completions.create(
    model="Qwen/Qwen3-4B-Instruct-2507",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=200,
)

print(response.choices[0].message.content)
