import os
import streamlit as st


cwd = os.getcwd()

welcome_page = st.Page(page=os.path.join(cwd, "welcome.py"), title="Welcome page")
documentation_rag = st.Page(page=os.path.join(cwd, "documentation_rag.py"), title="Ask Questions About AELF Actively")
chart_py = st.Page(page=os.path.join(cwd, "chart_explain.py"), title="Upload Chart and get explanation")
code_bender = st.Page(page=os.path.join(cwd, "code_bender.py"), title="Generate blockchain code")


pg = st.navigation(pages=[welcome_page, documentation_rag, chart_py, code_bender])
st.set_page_config(page_title="Welcome Page")

pg.run()