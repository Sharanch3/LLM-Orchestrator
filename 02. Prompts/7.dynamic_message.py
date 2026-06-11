from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()


chat_tempalte = ChatPromptTemplate([
    ('system',"You are a helpful {domain} expert."),
    ('human',"Expain in Layman's term, what is {topic}.")
   
])

prompt = chat_tempalte.invoke({"domain":'cricket expert',"topic":'Dusra'})

print(prompt)
