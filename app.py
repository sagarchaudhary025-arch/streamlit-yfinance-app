import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="YFinance App", layout="wide")

st.title("YFinance Data Fetching App")

ticker = st.text_input("Enter stock ticker", "AAPL")
period = st.selectbox("Select period", ["1mo", "3mo", "6mo", "1y", "5y"])
interval = st.selectbox("Select interval", ["1d", "1wk", "1mo"])

if ticker:
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)

    if not hist.empty:
        st.subheader(f"Historical Data for {ticker}")
        st.dataframe(hist.tail(10))

        fig = px.line(hist, x=hist.index, y="Close", title=f"{ticker} Closing Price")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data found. Try another ticker.")
