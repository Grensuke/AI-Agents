from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b", temperature = 0.3)

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

SYSTEM = """ROLE:   You are the friendly assistant for Sweet Crumbs Home Bakery.
FACTS:  Plum cake Rs 500. Chocolate cake Rs 650. Cupcake Rs 80 each.
        Orders need 24 hours' notice. All cakes have eggless versions.
RULES:  Never promise a delivery time or place. If it isn't in FACTS,
        say "I'll check with the owner." Work out totals carefully.
FORMAT: Under 50 words, friendly, English or Telugu matching the customer."""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("history"),          # the chat so far goes here
    ("human", "{question}"),
])
chain = prompt | llm | StrOutputParser()

history = []

def ask(question: str) -> str:
    answer = chain.invoke({"history": history, "question": question})
    history.extend([("human", question), ("ai", answer)])
    return answer

# while (1):
#     s = input()
#     if (s == 'bye'):
#         break
#     print(ask(s))

# print(ask("Hi, I'm Ravi. Do you make eggless cakes?"))
# print(ask("What's my name?"))

import csv
from pathlib import Path

def run_tests(path: str = "tests.csv") -> None:
    test_path = Path(path)
    if not test_path.is_absolute():
        test_path = Path(__file__).resolve().parent / test_path
    with test_path.open(newline="", encoding="utf-8") as test_file:
        rows = list(csv.DictReader(test_file))
    passed = 0
    for row in rows:
        answer = chain.invoke({"history": [], "question": row["question"]})
        ok = row["must_include"].lower() in answer.lower()
        passed += ok
        print("PASS" if ok else "FAIL", "|", row["question"], "->", answer[:70])
    print(f"\n{passed}/{len(rows)} passed ({passed / len(rows):.0%})")

run_tests()