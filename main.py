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
ticker_list = pd.read_csv('https://github.com/omkarkanchi/cloudomiee/blob/83319a263aee19677ee179b806488c4190082a63/nifty50.csv')
yahoo_symbols = ticker_list.Yahoo_Symbol.to_list()
tickerSymbol = st.sidebar.selectbox('Stock ticker', yahoo_symbols) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

