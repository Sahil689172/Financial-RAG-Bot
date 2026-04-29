import yfinance as yf
import pandas as pd


def get_stock_data(symbol):
    """
    Download stock data and normalize columns
    """

    df = yf.download(
        symbol,
        period="3mo",
        interval="1d",
        auto_adjust=True
    )

    if df.empty:
        raise ValueError("No stock data found")

    # Fix MultiIndex issue from yfinance
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df