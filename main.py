import logging
from data_fetcher import fetch_data
from indicators import calculate_rsi, calculate_moving_averages
from strategy import generate_signals
from ml_model import train_predictor
from csv_handler import log_trades, summarize_pnl


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_algo_trader():
    tickers = ["RELIANCE.NS", "INFY.NS", "TCS.NS"]
    all_signals = []

    for ticker in tickers:
        try:
            logging.info(f"Fetching data for {ticker}")
            df = fetch_data(ticker)

            logging.info("Calculating indicators")
            df = calculate_rsi(df)
            df = calculate_moving_averages(df)

            logging.info("Generating trade signals")
            signals = generate_signals(df)
            all_signals.extend([(ticker, *s) for s in signals])

            logging.info("Training ML model for prediction")
            model, acc = train_predictor(df)
            logging.info(f"{ticker} model accuracy: {acc:.2%}")

        except Exception as e:
            logging.error(f"Error processing {ticker}: {e}")

    if all_signals:
        logging.info(f"Logging {len(all_signals)} signals to CSV")
        log_trades(all_signals)

        logging.info("Generating PnL summary")
        summarize_pnl()

    else:
        logging.info("No trade signals generated.")

if __name__ == "__main__":
    run_algo_trader()
