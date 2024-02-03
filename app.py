import streamlit as st
import os
import requests

import numpy as np
import pandas as pd


name = st.selectbox(
    'Who is this?',
    ('Arnaud', 'Arnaud', 'Arnaud'))


st.markdown(f"""# This is a {name}
## This is a sub header
This is text
            
1. one
2. two
3. three""")

@st.cache
def df():
 return pd.DataFrame({
        'first column': list(range(1, 11)),
        'second column': np.random.randint(100, size=10)
    })

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
h = df().head(line_count)
h

st.markdown(f"\nAPI_KEY={os.environ.get('API_KEY')}")

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.markdown(key)


api_url = 'mysupermodel.com/predict'
res = requests.get(api_url)
st.markdown(res.json())