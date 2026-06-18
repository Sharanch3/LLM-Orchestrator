# to convert custome funtion of Python into runnable
# it will behave as a runnable and can be used during chaining process


from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)


# def word_counter(text):
#     return len(text.split())


# runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke("HI there how are you?"))



prompt = PromptTemplate(
    template="Write a joke about a {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

#Funtion
# def word_count(text):
#     return len(text.split())


joke_gen_chain = RunnableSequence(prompt , model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x:len(x.split()))
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

response = final_chain.invoke({'topic':'AI'})

print(response)