
import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write(""" Focus on discussing the company's offerings, significant company milestones and aspects of the vision 
    and values that connect with your professional and personal aspirations. You can describe how the organisation can benefit from your ideas in increasing revenue or brand recognition.
""")

st.subheader("Our Team")

col1,col2,col3= st.columns(3)

df=pandas.read_csv("data (2).csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images (2)/"+ row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images (2)/"+ row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images (2)/"+ row["image"])