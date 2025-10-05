from Stonks.data_fetch import fetch_historic_data
from Stonks.indicators import sma, rsi, volume_spike, pct_off_52w_high, crossover_above
from Stonks.alerts import check_alerts
TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "NLR", "OKLO", "NFLX", "META"]

def compute_indicators(df):
    df['SMA50'] = sma(df['Close'], window=50)
    df['SMA200'] = sma(df['Close'], window=200)
    df['RSI14'] = rsi(df['Close'], period=14)
    df['VolSpike'] = volume_spike(df['Volume'], window=20)
    df['PctOffHigh'] = pct_off_52w_high(df['Close'], lookback=252)
    df['GoldenCross'] = crossover_above(df['SMA50'], df['SMA200'])
    return df

def main():
    all_alerts = []
    for ticker in TICKERS:
        print(f"Fetching data for {ticker}...")
        df = fetch_historic_data(ticker, period='1y', interval='1d')
        if df.empty:
            print(f"No data found for {ticker}. Skipping.")
            continue
        df = compute_indicators(df)
        alerts = check_alerts(df, ticker)
        all_alerts.extend(alerts)

    if all_alerts:
        print("Alerts:")
        for alert in all_alerts:
            print(alert)
    else:
        print("No alerts generated.")

if __name__ == "__main__":
    main()
