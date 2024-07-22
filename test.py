#from dotenv import load_dotenv
#load_dotenv()

import time
from langchain_openai import ChatOpenAI
import streamlit as st

llm = ChatOpenAI()

st.title("AI POET")
content = st.text_input("Write a content")

   



if st.button("GO WRITE"):
    with st.spinner('Wait for it...'):
        result = llm.invoke("write a poet about "+content)
    
        st.write("The title of a poem is", content)
        st.write(result.content)