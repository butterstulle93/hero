import time
import numpy as np
import streamlit as st


last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101000000000000000000000000):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    
    last_rows = new_rows
    time.sleep(1)
    st.write(i + " " + "Versuch")

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
