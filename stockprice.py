import streamlit as st
import pandas_datareader as pdr

st.write('show the stock price of SAMSUNG')

df = pdr.get_data_yahoo('005930.KS','2022-01-01','2022-03-20')

st.line_chart(df.Close)
st.line_chart(df.Volume)
