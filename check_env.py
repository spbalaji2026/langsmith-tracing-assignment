import os
from dotenv import load_dotenv
load_dotenv()

print("Tracing :", os.getenv("LANGSMITH_TRACING"))
print("Project :", os.getenv("LANGSMITH_PROJECT"))
print("LS key set  :", bool(os.getenv("LANGSMITH_API_KEY")))
print("OpenAI key set:", bool(os.getenv("OPENAI_API_KEY")))