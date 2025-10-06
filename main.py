from Stonks.data_fetch import fetch_historic_data, fetch_current_price
from Stonks.indicators import sma, rsi, volume_spike, pct_off_52w_high, crossover_above
from Stonks.alerts import check_alerts
from Stonks.utils import send_telegram_message

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "NLR", "OKLO", "NFLX", "META","PLTR", "SHLD"]

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

        # Fetch historical data for indicators
        df = fetch_historic_data(ticker)
        if df.empty:
            print(f"No data found for {ticker}. Skipping.")
            continue
        df = compute_indicators(df)

        # Fetch current price and timestamp
        current_price, current_ts = fetch_current_price(ticker)
        if current_price is None or current_ts is None:
            print(f"No current price data for {ticker}. Skipping.")
            continue

        # Check for alerts
        alerts = check_alerts(df,current_price, current_ts, ticker)
        if alerts:
         all_alerts.append(alerts)

    # Print all alerts
    if all_alerts:
        msg_lines =["\n 🚨 Alerts: \n"]
        for alert in all_alerts:
            ts_str = alert['timestamp'].strftime("%d/%m/%Y %H:%M")
            msg_lines.append(f"{alert['ticker']} - Last price: ${alert['last_price']:.2f} (@ {ts_str})")
            for msg in alert['alerts']:
                msg_lines.append(f"  ‣ {msg}")
        send_telegram_message("\n".join(msg_lines))

if __name__ == "__main__":
    main()
