#!/usr/bin/env python
# coding: utf-8

# In[13]:


import streamlit as st
import pandas as pd
import numpy as np


# In[ ]:





# In[17]:


import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px


# In[20]:


fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig2 = px.scatter(x=[9, 1, 0, 3, 4], y=[10, 8, 2, 1, 0])



# In[21]:


st.title('Uber pickups in NYC')



col1, col2  = st.beta_columns(2)

with col1:
    st.header("A cat")
    st.plotly_chart(fig)

with col2:
    st.header("A dog")
    st.plotly_chart(fig2)
    




    


# In[ ]:





# In[ ]:





# In[ ]:




