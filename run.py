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

    if returns.std() != 0:
        print("Sharpe:", round(sharpe_ratio(returns), 3))
    else:
        print("Sharpe: N/A")

    print("Max Drawdown:", round(max_drawdown(equity), 3))

    # =========================
    # 4) Buy & Hold comparison
    # =========================
    data['BuyHold'] = data['Close'].pct_change().fillna(0)
    data['BuyHold_Equity'] = (1 + data['BuyHold']).cumprod()

    # =========================
    # 5) Plot equity curve
    # =========================
    plt.figure(figsize=(10, 5))
    plt.plot(equity, label="Strategy")
    plt.plot(data['BuyHold_Equity'], label="Buy & Hold", linestyle='--')
    plt.title("Equity Curve Comparison")
    plt.xlabel("Time")
    plt.ylabel("Equity")
    plt.legend()
    plt.grid()

    # Save image (สำคัญมากสำหรับ GitHub)
    plt.savefig("equity_curve.png")

    plt.show()


if __name__ == "__main__":
    main()
