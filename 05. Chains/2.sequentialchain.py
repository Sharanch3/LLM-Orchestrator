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


prompt1 = PromptTemplate(
    template="Give a detial report on the topic {topic}.",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the {report} in concise way.",
    input_variables=['report']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({'topic':'Dota 2'})

print(response)