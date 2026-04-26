import numpy as np

def sharpe_ratio(returns):
    if returns.std() == 0:
        return 0
    return (returns.mean() / returns.std()) * np.sqrt(252)

def max_drawdown(equity):
    peak = equity.cummax()
    drawdown = (equity - peak) / peak
    return drawdown.min()
