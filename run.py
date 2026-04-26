import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from strategy import generate_signal
from backtest import backtest
from performance import sharpe_ratio, max_drawdown


def main():
    # =========================
    # 1) Load real market data
    # =========================
    data = yf.download("AAPL", start="2020-01-01", progress=False)
    data = data[['Close']].dropna()

    # =========================
    # 2) Run trading system
    # =========================
    data = generate_signal(data)
    data = backtest(data)

    # =========================
    # 3) Performance metrics
    # =========================
    returns = data['Strategy'].dropna()
    equity = data['Equity']

    print("Sharpe:", round(sharpe_ratio(returns), 3))
    print("Max Drawdown:", round(max_drawdown(equity), 3))

    # =========================
    # 4) Plot equity curve
    # =========================
    plt.figure(figsize=(10, 5))
    plt.plot(equity, label="Strategy Equity")
    plt.title("Equity Curve")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
