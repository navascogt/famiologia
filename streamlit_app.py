import streamlit as st
import pandas as pd
import numpy as np

st.write('Hello Streamlit World!')

with st.sidebar:
    st.header('About famiologia')
    st.write('This is my first app in Streamlit!')

st.header('This is a header with a divider', divider='rainbow')

st.markdown('This text is created with st.markdown')

col1, col2 = st.columns(2)

st.subheader('st.column')

with col1:
    x = st.slider('Select a value', 1, 20)

with col2:
    st.write(x, 'squared of :blue[***x***] is', x * x)

st.subheader('st.line_chart')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.subheader('st.area_chart')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.area_chart(chart_data)
