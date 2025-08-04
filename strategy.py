def generate_signals(df):
    signals = []
    for i in range(50, len(df)):
        if df['RSI'].iloc[i] < 30 and df['MA20'].iloc[i] > df['MA50'].iloc[i]:
            signals.append((df.index[i], "BUY", float(df['Close'].iloc[i])))
        elif df['RSI'].iloc[i] > 70 and df['MA20'].iloc[i] < df['MA50'].iloc[i]:
            signals.append((df.index[i], "SELL", float(df['Close'].iloc[i])))
    return signals
