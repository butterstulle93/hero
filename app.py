import streamlit as st
import pandas as pd


st.title("Ja es haaaaat endlich geklappt!!!!")
col1, col2, col3 = st.beta_columns(3)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Karl Ess 1", "Karl Ess", "KIZ")
)

if add_selectbox == "KIZ" :
    st.image("https://hiphop.de/sites/default/files/styles/hiphopde_800x450/public/news_articles/kiz_pr_2015_1600.jpg?itok=j7kBUwML")

elif add_selectbox == "Karl Ess":
    st.write("Lern erstmal die Basis")

else:
    st.write("Standard Karl")


with col1:
    st.image("https://yt3.ggpht.com/ytc/AAUvwnjv4fz3f0cP5DApmFWWyh3l8B6DMk9kU7NaIvQb8A=s900-c-k-c0x00ffffff-no-rj")

with col2:
    st.image("https://yt3.ggpht.com/ytc/AAUvwnjv4fz3f0cP5DApmFWWyh3l8B6DMk9kU7NaIvQb8A=s900-c-k-c0x00ffffff-no-rj")

with col3:
    st.image("https://yt3.ggpht.com/ytc/AAUvwnjv4fz3f0cP5DApmFWWyh3l8B6DMk9kU7NaIvQb8A=s900-c-k-c0x00ffffff-no-rj")



