import pandas as pd


def compute_ema(df, span=50):
    """
    Compute EMA (Exponential Moving Average)
    """
    df["EMA_50"] = df["Close"].ewm(span=span).mean()
    return df


def compute_rsi(df, period=14):
    """
    Compute RSI (Relative Strength Index)
    """
    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    return df


def detect_trend(df):
    """
    Detect trend using latest Close vs EMA
    """

    latest_close = df["Close"].values[-1]
    latest_ema = df["EMA_50"].values[-1]

    if latest_close > latest_ema:
        return "UPTREND"

    elif latest_close < latest_ema:
        return "DOWNTREND"

    return "SIDEWAYS"