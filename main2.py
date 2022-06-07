import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション:', condition



text = st.sidebar.text_input('あなたの趣味を推してください．')
'あなたの趣味:',text,'です．'

option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は', option,'です．'

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img,caption='ABC', use_column_width=True)