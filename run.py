import pandas as pd
from strategy import generate_signal
from backtest import backtest

# sample data
data = pd.DataFrame({
    'Close': [100,102,101,105,110,108,112]
})

data = generate_signal(data)
data = backtest(data)

print(data[['Close','Signal','Equity']])

import matplotlib.pyplot as plt

plt.plot(data['Equity'])
plt.title("Equity Curve")
plt.show()

from performance import sharpe_ratio

returns = data['Strategy'].dropna()
print("Sharpe:", sharpe_ratio(returns))

from performance import sharpe_ratio, max_drawdown

returns = data['Strategy'].dropna()
equity = data['Equity']

print("Sharpe:", sharpe_ratio(returns))
print("Max Drawdown:", max_drawdown(equity))
