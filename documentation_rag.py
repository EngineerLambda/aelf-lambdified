import os
import time
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_pinecone import PineconeVectorStore


secrets = st.secrets
# os.environ["GOOGLE_API_KEY"] = secrets["GOOGLE_API_KEY"]
ATLAS_URI = secrets["ATLAS_URI"]
DB_NAME = secrets["DB_NAME"]
COLLECTION_NAME = secrets["COLLECTION_NAME"]
INDEX_NAME = secrets["INDEX_NAME"]

st.set_page_config(page_title="Documentation AI", page_icon="📝")

# helper functions
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def stream_data(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)

llm = GoogleGenerativeAI(model="gemini-pro")
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

store = PineconeVectorStore(index_name="aelf-embed", embedding=embedding)
retriever = store.as_retriever()

prompt_template = """
Act as a question and answer agent for a blockchain documentation data, you are provided with this question
**question: {question}
and you are to use the provided context below to provide a context-aware answer, write out the context before trying to answer, if the provided information does not
contain the answer, tell the user you don't know. instead of saying 'according to the context', you can say 'according to AELF documentation'
**context: {context}
"""

prompt = PromptTemplate.from_template(prompt_template)
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


# chat interface for consistent queries
if "messages" not in st.session_state:
    welcome_message = "Hello there, I am a context aware AI model based on AELF documentation, ask your questions and I will be happy\
        to answer to the best of my ability"
    st.chat_message("ai").write_stream(stream_data(welcome_message))
    st.session_state.messages = []

# Display for all the messages
for message, kind in st.session_state.messages:
    with st.chat_message(kind):
        st.markdown(message)

prompt = st.chat_input("Ask your questions ...")

if prompt:
    # contexts = vector_search.similarity_search(prompt, k=100)
    # context_f = format_docs(contexts)
    # Handling prompts and rendering to the chat interface
    st.chat_message("user").markdown(prompt)
    # st.chat_message("human").markdown(f"**Context**:\n{context_f}")
    st.session_state.messages.append([prompt, "user"])  # updating the list of prompts

    with st.spinner("Generating response"):
        answer = rag_chain.invoke(prompt)
        if answer:
            st.chat_message("ai").write_stream(stream_data(answer))
            st.session_state.messages.append([answer, "ai"])