import streamlit as st
import pandas as pd
import numpy as np

st.title('Mi Dashboard Interactivo')

st.write("Aquí hay algunos datos interesantes:")

df = pd.DataFrame({
    'Column A': np.random.randn(10),
    'Column B': np.random.randn(10)
})

st.line_chart(df)