import yfinance as yf
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

if __name__ == "__main__":
    # Example usage
    ticker = "NVDA"
    data = fetch_historic_data(ticker, period='1y', interval='1d')
    print(data.tail())