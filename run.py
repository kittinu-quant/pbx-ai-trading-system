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

data = backtest(data)

plt.plot(data['Equity'])
plt.title("Equity Curve")
plt.show()
