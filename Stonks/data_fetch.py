import yfinance as yf
from datetime import datetime, date
import pandas as pd

def fetch_historic_data(ticker, period='2y', interval='1d'):
    """
    Fetch historical stock data for a given ticker symbol.

    Parameters:
    ticker (str): The stock ticker symbol.
    period (str): The pecd riod over which to fetch data (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    interval (str): The data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo').

    Returns:
    pd.DataFrame: A DataFrame containing the historical stock data.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist

def fetch_current_price(ticker):
    """
    Fetch the current stock price for a given ticker symbol.

    Parameters:
    ticker (str): The stock ticker symbol.

    Returns:
    float: The current stock price.
    timestamp: The timestamp of the current price.
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period='1d', interval='5m')
    if df.empty:
        return None, None

    latest_row = df.iloc[-1]
    price = latest_row['Close']
    ts = latest_row.name.to_pydatetime()

    return price, ts
if __name__ == "__main__":
    # Example usage
    ticker = "NVDA"
    data = fetch_historic_data(ticker, period='1y', interval='1d')
    print(data.tail())