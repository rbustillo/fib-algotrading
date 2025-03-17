# 📈 Senior Math Project: Automated Algorithmic Trading

## 🎯 Project Goal
This project develops a Python-based automated algorithmic trading system that leverages **Fibonacci retracements, moving averages, and the Relative Strength Index (RSI)** to make trading decisions. The system is designed to identify **buy** and **sell** signals based on technical indicators and applies **risk management strategies** to optimize profitability.

## 📌 Key Features
- **Fibonacci Retracements**: Identifies potential support and resistance levels using Fibonacci ratios (0.236, 0.382, 0.618).
  - 📉 **Buy Signal**: When the price retraces to a Fibonacci support level and shows signs of reversing upward.
  - 📈 **Sell Signal**: When the price hits a Fibonacci resistance level and reverses downward.

- **Moving Averages**: Detects market trends using short-term (9-day) and medium-term (21-day) moving averages.
  - 🔼 **Uptrend**: When the short-term moving average crosses above the long-term moving average.
  - 🔽 **Downtrend**: When the short-term moving average crosses below the long-term moving average.

- **Relative Strength Index (RSI)**: Measures momentum to detect overbought or oversold conditions.
  - 📈 **Overbought Condition**: RSI > 70 → Potential **Sell** signal.
  - 📉 **Oversold Condition**: RSI < 30 → Potential **Buy** signal.

- **Risk Management Strategies**:
  - ⛔ **Stop Loss**: Automatically exits a trade if the price drops **15%** below the entry point.
  - ✅ **Take Profit**: Locks in gains when the price rises **20%** above the entry point.
  - 🔄 **Trailing Stop Loss**: Adjusts stop-loss upward as the price increases by **5%**.

## 📊 Backtesting
The algorithm was tested on **SPY (S&P 500 ETF)** using historical data from **Jan 1, 2019 – Jan 1, 2024** with an initial capital of **$100,000**.

### 📉 Results
- The algorithm’s performance was compared against the overall market returns.
- **Key metrics** such as total return, Sharpe ratio, and drawdowns were analyzed.
