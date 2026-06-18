#RUNNABLE BRANCH -> For creating conditional chains; If else logic in the world of Langchain

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)


prompt1 = PromptTemplate(
    template="Write a detail report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the following text. \n{text}",
    input_variables=['text']
)

parser = StrOutputParser()


report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split()) > 100, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
    
)

final_chain = RunnableSequence(report_chain, branch_chain)

response = final_chain.invoke({'topic':'AI'})

print(response)