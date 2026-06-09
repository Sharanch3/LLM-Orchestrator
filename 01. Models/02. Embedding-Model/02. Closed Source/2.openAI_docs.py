from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)


documents = [
    "Delhi is the capital of India",
    "KAthmandu is the capital of Nepal",
    "PAris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(str(vector))