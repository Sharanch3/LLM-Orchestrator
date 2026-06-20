from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
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
    template="Answer the following question- \n{question} from the following text- \n{text}",
    input_variables=['text','question']
)

parser = StrOutputParser()


url = "https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDQ429/ref=sr_1_1_sspa?crid=12PAR8RSYZWH7&dib=eyJ2IjoiMSJ9.YzK0sRpQiVxQEhEv_1sNh7bQBcjdf266t00CWpmtBoRaCLcuCsyTdaJUxLIjiCKUfaB_SeOtPQIodQsGA8rSBFIqUqPzLxs7p68RSnDzoTzH1_wnxEZzj4TEMAzlNysytIl69iidR7rHU4forQqXezgGP7bs5fmGn_qfcMQ-8VPhspGOmI9wkfXudmNrkmwj9B3FaAm7svf2EVwEPJa7-goCg2051ilhOG_iKYf5_mk.orGX2RVeFfFWi61kD8zel4luaTfN8rO98iaRhxBpEhE&dib_tag=se&keywords=macbook&qid=1757247992&sprefix=macbook%2Caps%2C278&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

result = chain.invoke({'question':' what is the product we are talking about?','text':docs[0].page_content})

print(result)