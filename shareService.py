import streamlit as st
import numpy as np
import pandas as pd
#import requests

#df = pd.DataFrame({'ID':'boosterjae', 'numberOfChild' : 2, 'son' : 1, 'daughter': 1, 'ageOfChild'})
#df.to_csv('./customer.csv')



st.sidebar.title("같이 구해보아요!")
st.sidebar.write("카톡ID : boosterjae (개포8차)")
st.sidebar.write("3살~6살 애둘아빠")
service = st.selectbox("찾는 서비스",['이모님','선생님'])
if (service == '이모님') :
    service_detail = st.sidebar.selectbox("제안",['이모님 급구','저희 이모님 어때요?'])
    st.multiselect("요일", ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]) 
    st.select_slider(label='시간대',options=['오전7시', '오전8시', '오전9시','오전10시','오전11시','오전12시','오후1시','오후2시','오후3시','오후4시','오후5시','오후6시','오후7시','오후8시'], value=['오전9시','오후6시'])
if (service == '선생님') :
    service_detail = st.sidebar.selectbox("제안",['선생님 급구','이 선생님 어때요?'])

contents = st.sidebar.text_input(label='메모하기')

st.sidebar.button(label='올리기')
#freegeoip = "http://freegeoip.net/json"
#geo_r = requests.get(freegeoip)
#geo_json = geo_r.json()
df = pd.DataFrame(
     np.random.randn(3, 2) / [30, 30] + [37.51502, 127.01648],
     columns=['lat', 'lon'])


st.map(df)



