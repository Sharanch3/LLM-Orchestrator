from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

# passthrough = RunnablePassthrough()

# print(passthrough.invoke(2))


prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template="Explain the following joke. \n{text}",
    input_variables=['text']
)


parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt1, model , parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explantion':RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

response = final_chain.invoke({'topic':'Dota2'})

print(response['joke'])
print(response['explantion'])