from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template="Generate 5 lines interesting fact about {topic}.",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'topic':'Dota 2'})

# print(response)

chain.get_graph().print_ascii()  #to visualize chain 