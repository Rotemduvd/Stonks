def check_alerts(history_df, current_price, current_ts, ticker):
    """
    Generate alerts based on historical indicators and current price.
    history_df: daily data with SMA, RSI, etc.
    current_price: latest price (intraday or extended)
    current_ts: timestamp of current_price
    """
    alerts = []
    if history_df.empty or len(history_df) < 2 or current_price is None:
        return alerts

    latest_row = history_df.iloc[-1]
    prev_close = history_df['Close'].iloc[-2]

    # Significant price movement compared to previous close
    if (prev_close - current_price) / prev_close > 0.05:
        alerts.append(f"has dropped more than 5% from {prev_close:.2f} to {current_price:.2f}")
    if (current_price - prev_close) / prev_close > 0.05:
        alerts.append(f"has increased more than 5% from {prev_close:.2f} to {current_price:.2f}")

    # Price vs SMA
    if current_price <= latest_row["SMA50"]:
        alerts.append(f"price is below its 50-day SMA ({latest_row['SMA50']:.2f})")
    if current_price <= latest_row["SMA200"]:
        alerts.append(f"price is below its 200-day SMA ({latest_row['SMA200']:.2f})")

    # RSI signals
    if latest_row["RSI14"] <= 40:
        if latest_row["RSI14"] < 30:
            alerts.append(f"is oversold (RSI: {latest_row['RSI14']:.2f}).")
        else:
            alerts.append(f"is approaching oversold levels (RSI: {latest_row['RSI14']:.2f}).")

    # Golden Cross
    if latest_row.get("GoldenCross", False):
        alerts.append("has formed a Golden Cross 🏅 (SMA50 crossed above SMA200).")

    # Volume spike
    if latest_row.get("VolSpike", 0) >= 1.5 and latest_row["SMA50"] > latest_row["SMA200"]:
        alerts.append(f"📈 Volume spike ({latest_row['VolSpike']:.2f}× avg) in uptrend!")

    # 52-week high distance
    if latest_row.get("PctOffHigh", 0) < -20:
        alerts.append("is more than 20% off its 52-week high.")

    if alerts:
        return {
            "ticker": ticker,
            "last_price": current_price,
            "timestamp": current_ts,
            "alerts": alerts
        }
    else:
        return []