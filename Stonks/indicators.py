import pandas as pd
import numpy as np

def sma(series: pd.Series, window: int) -> pd.Series:
    """
    Calculate the Simple Moving Average (SMA) of a given series.

    Parameters:
    series (pd.Series): The input data series.
    window (int): The number of periods to calculate the SMA over.

    Returns:
    pd.Series: The SMA of the input series.
    """
    return series.rolling(window=window).mean()

def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI) of a given series.

    Parameters:
    series (pd.Series): The input data series.
    period (int): The number of periods to calculate the RSI over.

    Returns:
    pd.Series: The RSI of the input series.
    """
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100 / (1 + rs))
    return rsi

def volume_spike(volume: pd.Series, window: int = 20) -> pd.Series:
    """
    Identify volume spikes in a given volume series.

    Parameters:
    volume (pd.Series): The input volume series.
    window (int): The number of periods to calculate the moving average volume.

    Returns:
    pd.Series: A boolean series indicating where volume spikes occur.
    """
    avg_volume = volume.rolling(window=window, min_periods=window).mean()
    return volume / avg_volume

def pct_off_52w_high(series: pd.Series, lookback: int = 252) -> pd.Series:
    """
    Calculate the percentage off the 52-week high.

    Parameters:
    series (pd.Series): The input data series.
    lookback (int): The number of periods to look back for the 52-week high.

    Returns:
    pd.Series: The percentage off the 52-week high.
    """
    high_52w = series.rolling(window=lookback, min_periods=lookback).max()
    pct_off = (high_52w - series) / high_52w * 100
    return pct_off

def crossover_above(series1: pd.Series, series2: pd.Series) -> pd.Series:
    """
    Identify points where series1 crosses above series2.

    Parameters:
    series1 (pd.Series): The first input data series.
    series2 (pd.Series): The second input data series.

    Returns:
    pd.Series: A boolean series indicating where series1 crosses above series2.
    """
    return (series1 > series2) & (series1.shift(1) <= series2.shift(1))

def crossover_below(series1: pd.Series, series2: pd.Series) -> pd.Series:
    """
    Identify points where series1 crosses below series2.

    Parameters:
    series1 (pd.Series): The first input data series.
    series2 (pd.Series): The second input data series.

    Returns:
    pd.Series: A boolean series indicating where series1 crosses below series2.
    """
    return (series1 < series2) & (series1.shift(1) >= series2.shift(1))