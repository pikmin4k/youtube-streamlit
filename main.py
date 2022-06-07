import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

st.write('Dispray Image')

img= Image.open('sample.jpg')
st.image(img,caption='ABC', use_column_width=True)

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#st.table(df.style.highlight_max(axis=0))

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']

)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']

)
st.map(df)

"""
#  章
##  節
###  項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""