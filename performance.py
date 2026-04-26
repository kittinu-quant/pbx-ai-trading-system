import numpy as np

def sharpe_ratio(returns):
    return np.mean(returns) / np.std(returns) * np.sqrt(252)

def max_drawdown(equity):
    peak = equity.cummax()
    dd = (equity - peak) / peak
    return dd.min()
