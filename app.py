import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title("Mein erstes Dashboard")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

import pydeck as pdk

HEXAGON_LAYER_DATA = (
    "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"  # noqa
)

# Define a layer to display on a map
layer = pdk.Layer(
    "HexagonLayer",
    HEXAGON_LAYER_DATA,
    get_position=["lng", "lat"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=False,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1,
)

# Set the viewport location
view_state = pdk.ViewState(
    longitude=-1.415, latitude=52.2323, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36,
)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)




r.to_html("hexagon_layer.html")

col1, col2, col3 = st.beta_columns(3)

with col1: 
    st.pydeck_chart(r)
    

with col2: 
    st.pydeck_chart(r)

with col3: 
    st.pydeck_chart(r)



  
 
