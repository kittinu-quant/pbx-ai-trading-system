def generate_signal(data, short=20, long=50):
    data = data.copy()

    data['EMA_S'] = data['Close'].ewm(span=short).mean()
    data['EMA_L'] = data['Close'].ewm(span=long).mean()

    data['Signal'] = 0
    data.loc[data['EMA_S'] > data['EMA_L'], 'Signal'] = 1
    data.loc[data['EMA_S'] < data['EMA_L'], 'Signal'] = -1

    return data
