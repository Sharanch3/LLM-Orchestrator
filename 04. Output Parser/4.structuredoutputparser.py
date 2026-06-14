from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)


schema = [
    ResponseSchema(name='fact_1',description="Fact 1 about the topic"),
    ResponseSchema(name='fact_2',description="Fact 2 about the topic"),
    ResponseSchema(name='fact_3',description="Fact 3 about the topic")
    
]

parser =  StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about the {topic}.\n{format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

# prompt = template.invoke({'topic':'black hole'})

# response = model.invoke(prompt)

# print(parser.parse(response.content))

chain = template | model | parser

response = chain.invoke({'topic':'black hole'})

print(response)

#downside of the structured output parser is that we can enforce schema but data validation is not possible .
# there comes in the picture Pydantic output parser