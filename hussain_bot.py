from dotenv import load_dotenv
from openai import OpenAI
import os
from PyPDF2 import PdfReader
import gradio as gr


load_dotenv(override=True)

reader = PdfReader("data/Resume.pdf")
resume = ""
for page in reader.pages:
    resume += page.extract_text()

# print(resume)
gemini = OpenAI(api_key=os.getenv("GEMINI_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai")
name = "Hussain"

system_prompt = f"""You are acting as {name}. You are answering questions on {name}'s website, \
    particularly questions related to {name}'s career, background, skills and experience. \
    Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
    You are given {name}'s resume which you can use to answer questions. \
    Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
    If a question is not related to {name}, politely decline to answer. \
    If you don't know the answer to a question, say so honestly and politely. \
"""

system_prompt += f"""

Resume: {resume}
\n
"""
system_prompt += f"With this context, please chat with the user, always staying in character as {name}"

def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]        
    response = gemini.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages,
    )
    return response.choices[0].message.content
    
gr.ChatInterface(chat).launch()

# response = ollama.chat.completions.create(
#     model="llama3.2:1b",
#     messages=[
#         {"role": "user", "content": "What is the capital of France?"}
#     ]
# )

# print(response.choices[0].message.content)