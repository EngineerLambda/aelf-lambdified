import streamlit as st
import time
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

template = """
Given a query, kindly generate the required code for the task as per the requirement.
Also, ensure that the required task is related to crypto currency, blockchain, smart contract development and other related terms in general\
If not, you should respond that you are not able to generate the required code for the task. But if the out of context query is a greeting or farewell respond to the greeting

query: {query}
"""

prompt_template = PromptTemplate.from_template(template=template)

llm = GoogleGenerativeAI(model="gemini-pro")

chain = ({"query": RunnablePassthrough()}
         | prompt_template
         | llm
         | StrOutputParser()
         )

def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)
        
st.set_page_config(page_title="Code with AI", page_icon="🖥️")

# chat interface for consistent queries
if "code_messages" not in st.session_state:
    welcome_message = "Hello there, I am your blockchain coding companion, send me your query and I will be happy\
        to answer to the best of my ability"
    st.chat_message("ai").write_stream(stream_data(welcome_message))
    st.session_state.code_messages = []

# Display for all the messages
for message, kind in st.session_state.code_messages:
    with st.chat_message(kind):
        st.markdown(message)
        
# chat history function
def format_history(messages):
    history_template = ""
    for message, kind in messages:
        history_template += f"{kind}: {message}\n"
        
    return history_template
        

prompt = st.chat_input("Ask your questions ...")

if prompt:
    # Handling prompts and rendering to the chat interface
    st.chat_message("user").markdown(prompt)
    st.session_state.code_messages.append([prompt, "user"])  # updating the list of prompts

    with st.spinner("Generating response"):
        full_prompt = format_history(st.session_state.code_messages)
        answer = chain.invoke(full_prompt)
        if answer:
            st.chat_message("ai").write_stream(stream_data(answer))
            st.session_state.code_messages.append([answer, "ai"])
