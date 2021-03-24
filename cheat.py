import streamlit as st
import pandas as pd

col1, col2, col3 = st.beta_columns(3)

col1.subheader('Magic commands')
col1.code('''# Magic commands implicitly `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'dataframe:', data
    ''')


col2.subheader('Magic commands')
col2.code('''# Magic commands implicitly `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'dataframe:', data
    ''')


col2.subheader('Magic commands')
col1.code('''# Magic commands implicitly `st.write()`
\'\'\' _This_ is some __Markdown__ \'\'\'
a=3
'dataframe:', data
    ''')