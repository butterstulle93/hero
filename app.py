import streamlit as st
import pandas as pd

st.write("Hello, Heroku!")

df = pd.read_csv("hallo.csv")

st.write(df)


add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)



i = 101
while i < 101:
  st.write(i)
  
  
 
