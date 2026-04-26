import pandas as pd

def generate_signal(data):
    data['EMA20'] = data['Close'].ewm(span=20).mean()
    data['EMA50'] = data['Close'].ewm(span=50).mean()

    data['Signal'] = 0
    data.loc[data['EMA20'] > data['EMA50'], 'Signal'] = 1
    data.loc[data['EMA20'] < data['EMA50'], 'Signal'] = -1

    return data
