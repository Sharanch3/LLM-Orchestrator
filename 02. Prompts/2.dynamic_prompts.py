from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)


st.header("Research Tool")


paper_input = st.selectbox("Select Research Paper:",["Attention is all you need","Diffusion model","Transformer","BERT"])

style_input = st.selectbox("Select Explanation style:",["Layman's term","Math heavy","Code oriented","PHD level"])

length_input = st.selectbox("Select Explanation length:",["short", "medium","long"])

#Template
template = load_prompt('template.json')


if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input':style_input,
    'length_input':length_input
})


    st.divider()

    st.write(result.content)