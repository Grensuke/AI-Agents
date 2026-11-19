from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
# groq_api_key=os.getenv("groq_api_key")

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),        # who you are, who pays
    base_url = "https://api.groq.com/openai/v1",   # send requests to Groq, not OpenAI
)

SYSTEM = """ROLE:   You are the assistant for Sweet Crumbs Home Bakery.
FACTS:  We bake to order. Orders need 24 hours' notice. All cakes have eggless versions.
        Plum cake Rs 500. Chocolate cake Rs 650. Cupcake Rs 80.
FORMAT: Under 50 words, friendly, English or Telugu matching the customer."""


history = [{"role": "system", "content": SYSTEM}]
MAX_TURNS = 6  

def chat(user_text: str) -> str:
    history.append({"role": "user", "content": user_text})
    recent = [history[0]] + history[1:][-MAX_TURNS:] # system + last few
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b", messages=recent, temperature=0.3)
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply


while (1):
    s = input()
    print(chat(s))


