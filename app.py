import streamlit as st
import pandas as pd

st.write("Hello, Heroku!")

df = pd.read_csv("hallo.csv")

st.write(df)
