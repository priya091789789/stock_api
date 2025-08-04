import yfinance as yf

def fetch_data(ticker: str, period="6mo", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval)
    return df.dropna()
