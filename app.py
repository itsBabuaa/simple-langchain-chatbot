import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please respond to the question asked.'),
        ('user', 'Question:{que}')
    ]
)

# Gemma3
llm = Ollama(model = 'gemma3:4b')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# Streamlit UI
st.title('🗨️Simple Chat Bot')
st.markdown('Powered By - LangChain & Gemma 3')

input_text = st.text_input('🧑‍🏫Ask any question on your mind!')

if input_text:
    st.write(chain.invoke({'que':input_text}))