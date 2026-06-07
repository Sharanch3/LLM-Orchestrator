from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    temperature= 1.5
    
)


model = ChatHuggingFace(llm = llm)

response = model.invoke("What is the capital of India?")

print(response.content)