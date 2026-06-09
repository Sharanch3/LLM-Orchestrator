from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)

documents = [
    "New Delhi is the capital of India",
    "Paris is the capital of France",
    "KAthmandu is the capital of Nepal"
]

vector = embedding.embed_documents(documents)

print(str(vector))