from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o",temperature=1.2,max_completion_tokens=10)

response = model.invoke("What is the capital of India?")

print(response.content)