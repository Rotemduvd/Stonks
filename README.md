<p align="center">
  <img src="./assets/stonks.jpeg" alt="Stonks Meme">
</p>

# Stonks — Automated Stock Alert Bot

**Stonks** is a Python-based system that automatically checks several big-tech stocks each day,
calculates key technical indicators, and sends alerts to Telegram when conditions are met.

It runs via **GitHub Actions** (3× daily, Mon–Fri)
---

## 🚀 Features

* Fetches daily & intraday stock data using [`yfinance`](https://pypi.org/project/yfinance/)
* Calculates:

  * 50-day & 200-day **Simple Moving Averages (SMA)**
  * **RSI(14)** (Relative Strength Index)
  * **Volume spikes** (vs. 20-day average)
  * **% off 52-week high**
  * **Golden Cross** detection
  * Check out **Stonks** on Telegram — just search for "Stonks" to see the bot in action!
* Triggers alerts for conditions like:

  * Price < SMA(50) and RSI < 30
  * Volume spike during uptrend
  * Sharp daily moves (>5%)
* Sends alerts via **Telegram Bot API**
* Runs automatically via **GitHub Actions**
  (e.g. at 15:00, 19:00, and 00:00 IL time — 12:00, 16:00, and 21:00 UTC)
* Optional manual run via `/run` command on Telegram 🚀

---

## 🧠 Example Telegram Alert

```
🚨 Stock Alerts (06/10/2025 09:45)

📉 AMZN — $216.38
• Price below 50-day SMA (226.30)
• Approaching oversold (RSI: 37.9)

📉 META — $692.80
• Price below 50-day SMA (751.90)
• Oversold (RSI: 29.65)
```

---

## 🗂️ Project Structure

```
Stonks/
│
├── Stonks/
│   ├── __init__.py
│   ├── data_fetch.py        # Fetch historical & current data
│   ├── indicators.py        # Calculate SMA, RSI, volume, etc.
│   ├── alerts.py            # Evaluate alert conditions
│   ├── utils.py             # Telegram integration & helpers
│
├── main.py                  # Entry point — runs checks & sends alerts
├── requirements.txt         # Dependencies
├── .github/
│   └── workflows/
│       └── alerts.yml       # GitHub Actions workflow (auto scheduler)
└── README.md
```

---

## ⚙️ Setup (Local Run)

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/Stonks.git
   cd Stonks
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv_stonks
   source venv_stonks/bin/activate  # macOS/Linux
   venv_stonks\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your environment variables**

   ```bash
   export TELEGRAM_BOT_TOKEN="your_token_here"
   export TELEGRAM_CHAT_ID="your_chat_id_here"
   ```

5. **Run manually**

   ```bash
   python main.py
   ```

---

## ⚙️ GitHub Actions Setup

1. Go to your repo → **Settings → Secrets and variables → Actions**
2. Add these secrets:

   * `TELEGRAM_BOT_TOKEN`
   * `TELEGRAM_CHAT_ID`
3. (Optional) add:

   * `GITHUB_PAT` (for Telegram-triggered runs)
4. Check `.github/workflows/alerts.yml` for schedule and adjust cron as needed.

**Default Schedule (UTC):**

```yaml
- cron: '0 12 * * 1-5'   # 15:00 IL — pre-market
- cron: '0 16 * * 1-5'   # 19:00 IL — mid-session
- cron: '0 21 * * 1-5'   # 00:00 IL — after close
```

---

## 🦯 GitHub Actions Usage

* Free accounts get **2,000 minutes/month**.
* Each run ≈ 30–40 seconds.
* 3 daily scheduled runs × 5 days × 4 weeks = **~30 minutes/month total**.
* You can safely trigger up to **~100 manual runs/day** from Telegram before hitting your cap.

---

## 👨🏼‍💻 Tech Stack

| Component      | Purpose                   |
| -------------- | ------------------------- |
| Python 3.12    | Core logic                |
| yfinance       | Market data               |
| pandas         | Indicators & calculations |
| requests       | Telegram + API calls      |
| GitHub Actions | Scheduler & runner        |

---

## 📜 License

MIT License © 2025 [Rotem Duvdevani](https://github.com/RotemDuvdevani)


