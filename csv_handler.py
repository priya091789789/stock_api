import pandas as pd
from pathlib import Path

TRADE_LOG_PATH = Path("trade_log.csv")
PNL_SUMMARY_PATH = Path("pnl_summary.csv")

def log_trades(trades: list):
    df = pd.DataFrame(trades, columns=["Ticker", "Date", "Signal", "Price"])
    if TRADE_LOG_PATH.exists():
        df.to_csv(TRADE_LOG_PATH, mode='a', header=False, index=False)
    else:
        df.to_csv(TRADE_LOG_PATH, index=False)

def summarize_pnl():
    if not TRADE_LOG_PATH.exists():
        print("No trades to summarize.")
        return

    df = pd.read_csv(TRADE_LOG_PATH)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
   
    df.dropna(subset=['Date', 'Price'], inplace=True)

   
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df.dropna(subset=['Price'], inplace=True)

    df.sort_values(by=["Ticker", "Date"], inplace=True)

    summary = []
    for ticker in df['Ticker'].unique():
        ticker_trades = df[df['Ticker'] == ticker]
        buy_prices = ticker_trades[ticker_trades['Signal'] == 'BUY']['Price'].tolist()
        sell_prices = ticker_trades[ticker_trades['Signal'] == 'SELL']['Price'].tolist()
        
        pnl = 0.0
        wins = 0
        num_trades = min(len(buy_prices), len(sell_prices))
        
        for b, s in zip(buy_prices, sell_prices):
            trade_pnl = s - b
            pnl += trade_pnl
            if trade_pnl > 0:
                wins += 1

        win_ratio = wins / num_trades if num_trades > 0 else 0
        summary.append({
            "Ticker": ticker,
            "Net PnL": round(pnl, 2),
            "Win Ratio": round(win_ratio, 2)
        })

    pd.DataFrame(summary).to_csv(PNL_SUMMARY_PATH, index=False)
