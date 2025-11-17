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
        alerts.append(f"ירד ביותר מ־5% מ־{prev_close:.2f} ל־{current_price:.2f}")
    if (current_price - prev_close) / prev_close > 0.05:
        alerts.append(f"עלה ביותר מ־5% מ־{prev_close:.2f} ל־{current_price:.2f}")

    # Price vs SMA
    if current_price <= latest_row["SMA50"]:
        alerts.append(f"המחיר נמוך מהממוצע הנע ל־50 יום ({latest_row['SMA50']:.2f})")
    if current_price <= latest_row["SMA200"]:
        alerts.append(f"המחיר נמוך מהממוצע הנע ל־200 יום ({latest_row['SMA200']:.2f})")

    # RSI signals
    if latest_row["RSI14"] <= 40:
        if latest_row["RSI14"] < 30:
            alerts.append(f"נמצא במכירת יתר (RSI: {latest_row['RSI14']:.2f}).")
        else:
            alerts.append(f"מתקרב לרמות של מכירת יתר (RSI: {latest_row['RSI14']:.2f}).")

    # Golden Cross
    if latest_row.get("GoldenCross", False):
        alerts.append("יצר 'גולדן קרוס' 🏅 (הממוצע הנע 50 חצה מעלה את 200).")

    # Volume spike
    if latest_row.get("VolSpike", 0) >= 1.5 and latest_row["SMA50"] > latest_row["SMA200"]:
        alerts.append(f"📈 עלייה חדה בנפח ({latest_row['VolSpike']:.2f}× מהממוצע) במהלך מגמת עלייה!")

    # 52-week high distance
    if latest_row.get("PctOffHigh", 0) < -20:
        alerts.append("נמצא יותר מ־20% מתחת לשיא של 52 שבועות.")

    if alerts:
        return {
            "ticker": ticker,
            "last_price": current_price,
            "timestamp": current_ts,
            "alerts": alerts
        }
    else:
        return []