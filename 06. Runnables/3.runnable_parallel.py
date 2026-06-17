from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

llm  = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm )


parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkedIN post about {topic}",
    input_variables=['topic']
)


parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'Linkedin': RunnableSequence(prompt2, model, parser)
})


response = parallel_chain.invoke({'topic':'AI'})

print(response['tweet'])
print("\n")
print(response['Linkedin'])