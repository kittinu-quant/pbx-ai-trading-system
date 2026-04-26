import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

from backtest import backtest

def generate_signal(data, short_window, long_window):
    data['EMA_short'] = data['Close'].ewm(span=short_window).mean()
    data['EMA_long'] = data['Close'].ewm(span=long_window).mean()

    data['Signal'] = 0
    data.loc[data['EMA_short'] > data['EMA_long'], 'Signal'] = 1
    data.loc[data['EMA_short'] < data['EMA_long'], 'Signal'] = -1

    return data

def sharpe_ratio(returns):
    if returns.std() == 0:
        return 0
    return np.sqrt(252) * returns.mean() / returns.std()

def optimize(symbol="AAPL"):
    data = yf.download(symbol, start="2020-01-01", progress=False)
    data = data[['Close']].dropna()

    short_range = range(5, 50, 5)
    long_range = range(20, 200, 10)

    heatmap = np.zeros((len(short_range), len(long_range)))

    for i, short in enumerate(short_range):
        for j, long in enumerate(long_range):
            if short >= long:
                heatmap[i, j] = np.nan
                continue

            df = data.copy()
            df = generate_signal(df, short, long)
            df = backtest(df)

            returns = df['Strategy'].dropna()
            heatmap[i, j] = sharpe_ratio(returns)

    plt.figure(figsize=(12,6))
    plt.imshow(heatmap, aspect='auto', cmap='coolwarm')
    plt.colorbar(label='Sharpe')

    plt.xticks(range(len(long_range)), long_range, rotation=90)
    plt.yticks(range(len(short_range)), short_range)

    plt.xlabel("Long EMA")
    plt.ylabel("Short EMA")
    plt.title(f"Sharpe Heatmap ({symbol})")

    plt.savefig("heatmap.png")
    plt.show()

if __name__ == "__main__":
    optimize("AAPL")
