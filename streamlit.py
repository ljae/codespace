from pickletools import markobject
import pandas as pd
import streamlit as st
import pandas as pd
import pandas_datareader as pdr
from pandas_datareader import data 
import FinanceDataReader as fdr
import datetime as dt
import plotly.graph_objects as go
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


#df_nasdaq = fdr.StockListing('NASDAQ')
#df_amex = fdr.StockListing('AMEX')
#df_nyse = fdr.StockListing('NYSE')
#nasdaq = df_nasdaq.Symbol.tolist()
#amex = df_amex.Symbol.tolist()
#nyse = df_nyse.Symbol.tolist()
#tickers = nasdaq + amex + nyse

#df_marketCap = data.get_quote_yahoo(tickers)['MarketCap'].sort_values(ascending=False)

st.sidebar.header("**Jordan Rule For Esther**")
#side bar user input
startDate = st.sidebar.date_input('Start Date', dt.date(2021,1,1))
endDate = st.sidebar.date_input('End Date', dt.datetime.now())
#side bar select options
point = st.sidebar.selectbox("Quantitative Easing Status Point (%)",['2.5','5'])

range_num = 11 

#get a price of AAPL thorugh pandas_Datareader
df = fdr.DataReader(symbol='AAPL',start=startDate, end=endDate)
highest = df.sort_values(by='Close',ascending=False)['Close'][0]

invest_point = pd.DataFrame(columns=['##Slot##','##Price##','#Asset#'])

invest_point['#Check#'] = False

invest_point.head()

current_price = df['Close'][-1]


st.title("Private Finance Management Tool")
st.header("Stock Price of APPLE : "+str(current_price))



#str to integer
point = float(point)/100


for i in range(range_num):
  invest_point.loc[i,['##Slot##']] = str(round(point*i*100,2))+'%'
  invest_point.loc[i,['##Price##']] = round(highest * (1-point*i) ,2)
  price_flag = round(highest * (1-point*i),2)
  n_price_flag = round(highest * (1-point*(i+1)),2)
  if price_flag > current_price and n_price_flag <= current_price :
    invest_point.loc[i,['#Check#']] = True
  price_flag = round(highest * (1-point*i),2)
  invest_point.loc[i,['#Asset#']] = str(10*i) + '%'



st.line_chart(df['Close'])

#coloring the table
#def highlight_survived(s):
    #return ['background-color: green']*len(s) if s['#Check#'] == True  else ['background-color: red']*len(s)

#st.dataframe(invest_point.style.apply(highlight_survived, axis=1))

gb = GridOptionsBuilder.from_dataframe(invest_point)
gb.configure_side_bar() #Add a sidebar
gridOptions = gb.build()

grid_response = AgGrid(
    invest_point,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='blue', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)



nasdaq_index = fdr.DataReader(symbol='IXIC', start=dt.datetime.now()-dt.timedelta(30))

continuous_ups = 0
for i in range(8):
  if nasdaq_index.iloc[-1*i-1]['Change'] > 0:
    continuous_ups= continuous_ups + 1
  else :
    break

bear_period = nasdaq_index.loc[nasdaq_index['Change']<-0.03]
invest_mode = pd.DataFrame(columns=['MODE','TERM'])
invest_mode.loc[0,'MODE'] = 'Rebalancing'
invest_mode.loc[0,'TERM'] = False
if len(bear_period) >= 1 :
  invest_mode.loc[0,'MODE'] = '말뚝박기'
  invest_mode.loc[0,'TERM'] = bear_period.index[-1] + dt.timedelta(31)
  if continuous_ups > 7:
    invest_mode.loc[0,'MODE'] = 'Rebalancing'
    invest_mode.loc[0,'TERM'] = bear_period.index[0] + dt.timedelta(31)
  if len(bear_period) >= 4 :
    invest_mode.loc[0,'MODE'] = '공항도래'
    invest_mode.loc[0,'TERM'] = bear_period.index[0] + dt.timedelta(61)

st.sidebar.markdown('**Mode of Investing**')
st.sidebar.markdown(invest_mode.MODE[0])
st.sidebar.markdown('**Last date of Nasdaq -3%**')
st.sidebar.markdown(bear_period.index[-1])
st.sidebar.markdown('**Start date of Investing**')
st.sidebar.markdown(invest_mode.TERM[0])

st.sidebar.markdown('**Countiuous Ups**')
st.sidebar.markdown(continuous_ups)

#Data Set
#countries=['India', 'Australia',
           #'Japan', 'America',
           #'Russia']
 
#values = [4500, 2500, 1053, 500,
          #3200]

##The plot
#fig = go.Figure(
    #go.Pie(
    #labels = countries,
    #values = values,
    #hoverinfo = "label+percent",
    #textinfo = "value"
#))

#st.header("Pie chart")
#st.plotly_chart(fig)