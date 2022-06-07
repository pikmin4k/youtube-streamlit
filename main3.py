import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

espander = st.expander('問い合わせ')
espander.write('問い合わせ内容を書く')