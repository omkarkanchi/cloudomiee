import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
st.markdown('''
# Stock Price App
Shown are the stock price data for query companies!
''')
st.write('---')
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2020, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))
ticker_list = pd.read_csv('nifty50.csv')
yahoo_symbols = ticker_list.Yahoo_Symbol.to_list()
tickerSymbol = st.sidebar.selectbox('Stock ticker', yahoo_symbols) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)
string_name = tickerData.info['longName']
st.header('**%s**' % string_name)
string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)
st.header('**Ticker data**')
st.write(tickerDf)
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
st.header('**Technical analysis chart**')
qf.add_sma([10,20],width=2,color=['green','lightgreen'],legendgroup=True)
qf.add_rsi(periods=20,color='java')
qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)
qf.add_volume()
qf.add_macd()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)