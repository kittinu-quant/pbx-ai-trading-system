import pandas as pd

def backtest(data):
    data['Return'] = data['Close'].pct_change()
    data['Strategy'] = data['Signal'].shift(1) * data['Return']

    data['Equity'] = (1 + data['Strategy']).cumprod()

    return data
