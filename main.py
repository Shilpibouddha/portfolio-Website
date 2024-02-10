import streamlit as st

st.set_page_config(layout="wide")

col1, col2 =st.columns(2)

with col1:
    st.image("images/photo.png" , width=300)

with col2:
    st.title("Shilpi Bouddha")
    content ="""
    Hi, I am shilpi! I am a python programmer and a Cyber Security Analyst.
    
    I am learning advance Python."""

    st.info(content)