# stock_api
# Mini Algo-Trading Prototype

This is a modular Python-based algorithmic trading prototype. It uses free stock market data to generate trade signals based on technical indicators (RSI and Moving Averages), logs trades in CSV files, performs simple machine learning-based prediction, and can optionally send Telegram alerts.

## Features

- Fetches historical stock data using `yfinance`
- Implements a rule-based trading strategy using:
  - RSI (Relative Strength Index)
  - 20-day and 50-day Moving Averages
- Logs trades and prices to CSV (`trade_log.csv`)
- Calculates net profit/loss (PnL) and win ratio (`pnl_summary.csv`)
- Trains a basic Decision Tree classifier using RSI, MACD, Volume
- Designed for backtesting over the last 6 months
- Optional: Sends trade alerts and error notifications to Telegram




## Trading Strategy Logic

**Buy Signal:**

- RSI is less than 30
- AND 20-day moving average is greater than 50-day moving average

**Sell Signal:**

- RSI is greater than 70
- AND 20-day moving average is less than 50-day moving average

The strategy is applied on a per-stock basis using the latest 6 months of data.

## Machine Learning (Optional Component)

- Features used: RSI, MA20, MA50, MACD, Volume
- Target: Whether the stock will close higher the next day
- Model: `DecisionTreeClassifier` from `scikit-learn`
- Output: Accuracy of prediction per stock

## Output Files

- `trade_log.csv`: Contains all trade signals with columns: `Ticker`, `Date`, `Signal`, `Price`
- `pnl_summary.csv`: Contains per-stock summary of net PnL and win ratio

## Telegram Alerts (Optional)

You can configure Telegram alerts for signal notifications and error reporting.

### Setup Instructions

1. Create a bot using [BotFather](https://t.me/BotFather) on Telegram.
2. Copy your bot token and start a chat with the bot.
3. Get your chat ID by sending a message to the bot and using:
