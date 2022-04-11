
from pickletools import markobject
import pandas as pd
import streamlit as st
import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import plotly.graph_objects as go
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

df = pd.read_csv('./siwon.csv')

#make a button on streamlit
if st.sidebar.button("Earn"):
    st.write('Select What you did for making money:')
    option_l = st.checkbox('Cleaning - Living Room (2,000)')
    option_p = st.checkbox('Cleaning - Play Room(2,000)')
    option_b = st.checkbox('Cleaning - Siwon\'s Bed Room(2,000)')
    option_d = st.checkbox('Help Washing dishes(500)')
    option_g = st.checkbox('Bring Garbage to dump(10,000)')
    if option_l :
        st.write("Wow Good boy, you cleaned up Living Room")
        df = df.append({'Date':dt.datetime.today(), 'Classify' : 'Earn', 'Price': 2000})
        df.to_csv('./siwon.csv')
