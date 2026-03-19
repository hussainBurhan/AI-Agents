from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(override=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")

# gemini = OpenAI(api_key=gemini_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# response = gemini.chat.completions.create(
#     model="gemini-2.5-flash-lite",
#     messages=[
#         {"role": "user", "content": "What is the capital of France?"}
#     ]
# )

# print(response.choices[0].message.content)

ollama = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = ollama.chat.completions.create(
    model="llama3.2:1b",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)



