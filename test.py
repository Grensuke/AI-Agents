from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b", temperature = 0.3)

# reply = llm.invoke([
#     ("system", "You are Sweet Crumbs assistant. Answer in under 30 words"),
#     ("human", "Do you make eggless cakes?"),
# ])
# print(reply.content)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the assistant for {business}. Answer in under 30 words."),
    ("human",  "{question}"),
])

from langchain_core.output_parsers import StrOutputParser

chain = prompt | llm | StrOutputParser()     # fill blanks → ask model → keep just the text
answer = chain.invoke({"business": "Petrol Bunk Assistant",
                       "question": "Do you make eggless cakes?"})
print(answer)











# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import json

# load_dotenv()
# # groq_api_key=os.getenv("groq_api_key")

# client = OpenAI(
#     api_key = os.getenv("GROQ_API_KEY"),        # who you are, who pays
#     base_url = "https://api.groq.com/openai/v1",   # send requests to Groq, not OpenAI
# )

# SYSTEM = """Extract the order from the customer's message.
# Return ONLY JSON, no other text, with these keys:
# name (text), item (text), qty (number), date (text), eggless (true/false)."""

# response = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     temperature=0.2,                              # facts and prices: keep it focused
#     messages=[{"role": "system", "content": SYSTEM},
#               {"role": "user",   "content": "Sravani: 6 cupcakes tmrw evening, normal with egg ok"}],
# )

# reply = response.choices[0].message.content     # a string that looks like JSON
# order = json.loads(reply)
# print(reply)                 # string → Python dict
# print(order["item"], order["qty"])               # plum cake 2
# text = json.dumps(order)
# print(text)








# dicts and json

# MENU = {"plum cake": 500, "chocolate cake": 650, "cupcake": 80}   # key → value

# MENU["plum cake"]                  # 500
# MENU.get("donut", "not on menu")   # 'not on menu'  (no crash)
# MENU["donut"]                      # KeyError: 'donut'  (crash!)

# order = {"name": "Ravi", "item": "plum cake", "qty": 2, "eggless": True}
# order["qty"] * MENU[order["item"]] # 1000

# import json
# text = json.dumps(order)           # dict → JSON string, to send or save
# back = json.loads(text)            # JSON string → dict