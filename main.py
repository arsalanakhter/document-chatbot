# So the idea is to have a streamlit app

import streamlit as st

st.set_page_config(page_title="Document ChatBot", page_icon=":tada:",
                   layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, This is a Document ChatBot :wave:")
    st.title("Document ChatBot")
    st.write(
        "The ChatBot takes as input a document and then we can "
        "ask questions from that document "
    )
    # st.write("[Learn More >](https://pythonandvba.com)")

# --- Button ---
# Add an upload button
with st.container():
    st.button('Upload')

