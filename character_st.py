from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

st.title("Batman")

template = """Question: {question}

Answer: """

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="Batman")
chain = prompt | model

if "history" not in st.session_state:
    st.session_state.history = []

question = st.chat_input("Speak Citizen")

if question:
    answer = chain.invoke({"question": question})
    st.session_state.history.append({"question": question, "answer": answer})

for i, entry in enumerate(st.session_state.history):
    st.write(f"**You :** {entry['question']}")
    st.write(f"**Batman :** {entry['answer']}")
