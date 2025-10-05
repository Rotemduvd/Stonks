def check_alerts(df, ticker):
    alerts = []
    if df.empty or len(df) < 2:
        return alerts

    latest_row = df.iloc[-1]
    prev_close = df['Close'].iloc[-2]

    # Check for significant price drop (e.g., more than 5%)
    if (prev_close - latest_row["Close"]) / prev_close > 0.05:
        alerts.append(f"{ticker} has dropped more than 5% from {prev_close:.2f} to {latest_row['Close']:.2f}")

    # Check for significant price increase (e.g., more than 5%)
    if (latest_row["Close"] - prev_close) / prev_close > 0.05:
        alerts.append(f"{ticker} has increased more than 5% from {prev_close:.2f} to {latest_row['Close']:.2f}")

    # Price below SMA50
    if latest_row["Close"] <= latest_row["SMA50"]:
        alerts.append(f"{ticker} price is below its 50-day SMA.")

    # Price is oversold or close to it (RSI < 30)
    if latest_row["RSI14"] <= 40:
        if latest_row["RSI14"] < 30:
            alerts.append(f"{ticker} is oversold (RSI: {latest_row['RSI14']:.2f}).")
        else:
            alerts.append(f"{ticker} is approaching oversold levels (RSI: {latest_row['RSI14']:.2f}).")

    # Golden Cross (SMA50 crosses above SMA200)
    if latest_row["GoldenCross"]:
        alerts.append(f"{ticker}: has formed a Golden Cross 🏅 (SMA50 crossed above SMA200).")

    # Volume spike + uptrend in price
    if latest_row["VolSpike"] >= 1.5 and latest_row["SMA50"] > latest_row["SMA200"]:
        alerts.append(f"{ticker}: 📈 Volume spike ({latest_row['VolSpike']:.2f}× avg) in uptrend!")

    # % off 52-week high
    if latest_row["PctOffHigh"] < -20:
        alerts.append(f"{ticker}: is more than 20% off its 52-week high.")

    return alerts