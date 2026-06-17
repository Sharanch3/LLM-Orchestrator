from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence #new

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)


prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template="Explain the following joke. \n{text}",
    input_variables=['text']
)


parser = StrOutputParser()


chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

response = chain.invoke({'topic':'AI'})

print(response)