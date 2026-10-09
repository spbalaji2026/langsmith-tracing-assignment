from dotenv import load_dotenv
load_dotenv()  # must come BEFORE the langchain import

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "In one sentence, what is the capital of Australia?",
    "Explain the difference between a list and a tuple in Python in 3 sentences.",
    "Write a detailed step-by-step guide of about 400 words on how to prepare for a data engineering job interview.",
]

for i, p in enumerate(prompts, start=1):
    print(f"\n--- Prompt {i}: {p}")
    print(llm.invoke(p).content)