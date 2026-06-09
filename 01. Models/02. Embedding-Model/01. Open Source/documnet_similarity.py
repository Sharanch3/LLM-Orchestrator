from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()


embedding = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)

documents = [
    "Sachin Tendulkar is the man who can beat any one",
    "Virat Kholi is the favourite batsman of 21st century",
    "Rohit Sharam is the friend of Virat",
    "Ganguli is the topntch crickter."
]

query = "Tell me about Virat Kholi"


doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)

print(scores)
