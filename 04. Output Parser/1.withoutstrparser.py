
#with result.content

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model =ChatHuggingFace(llm = llm)


#1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detail report on {topic}",
    input_variables=['topic']
)

#2nd prompt ->detailed summary
template2 = PromptTemplate(
    template="Write a five line summary on the following text./n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})
response1 = model.invoke(prompt1)


prompt2 = template2.invoke({'text': response1.content})
response2 = model.invoke(prompt2)

print(response2.content)