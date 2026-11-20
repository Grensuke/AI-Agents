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

SYSTEM = """ROLE:   You are the assistant for Petrol Bunk."""

# SYSTEM = "You are the assistant for Sweet Crumbs Home Bakery. Only answer the things related to sweet crumbs bakery."

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    temperature=0.2,                              # facts and prices: keep it focused
    messages=[{ "role": "system", "content": SYSTEM},
              {"role": "user", "content": "Can I get an eggless cake today evening?"}
              ],
)
print(response.choices[0].message.content)
#print(response.usage)