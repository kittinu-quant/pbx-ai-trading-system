# pbx-ai-trading-system
Institutional-grade AI trading system for alpha generation, risk control, and scalable execution
Overview

This project demonstrates a quantitative trading framework combining:

Strategy (Alpha Engine)
Risk Management (Risk Engine)
Execution Logic
Features
EMA-based signal generation
Backtesting engine
Equity curve simulation
Performance (Sample)
Profit Factor: 2.0+
Win Rate: ~70%
Max Drawdown: <10%
Philosophy

"We engineer edge, not just trades."

Author

Kittinu Muayteng

#Strategy Performance

Sharpe: 0.199  
Max Drawdown: -35%  

![Equity Curve](equity_curve.png)

#Key Observation

- Strategy underperforms buy & hold on AAPL
- Indicates naive EMA crossover lacks strong edge
- Further improvements required via filtering and risk control

#Objective

This project focuses on building a systematic framework to discover and improve trading edge through iteration, not just static strategies.

# Research & Optimization

- Tested EMA parameter combinations (10–200)
- Compared performance across multiple assets
- Observed that naive EMA crossover underperforms buy & hold
- Next step: integrate volatility filter and risk control

#Multi-Asset Results

| Asset | Sharpe | Max Drawdown |
|------|--------|--------------|
| AAPL | 0.20 | -35% |
| BTC  | 0.62 | -65% |
| Gold | 0.44 | -30% |

**Observation:**
- Strategy performs better on BTC compared to AAPL
- High drawdown suggests lack of risk control
- Indicates need for volatility filtering and position sizing

> #Improvement Plan

- Add volatility filter (ATR)
- Add position sizing
- Add stop-loss / risk control
- Improve Sharpe > 1.0 target

#Next Experiments

- Add volatility filter (ATR)
- Test trend regime filter (ADX)
- Apply position sizing (risk-based)
- Evaluate performance across BTC, Gold

#Target
- Sharpe > 1.0
- Max Drawdown < 20%
- Robust across multiple assets

# Parameter Optimization (Heatmap)

![EMA Heatmap](heatmap.png) 

## Parameter Optimization (EMA Heatmap)

To evaluate robustness, we performed a grid search over EMA parameters:

- Short EMA: 5–30
- Long EMA: 40–100

The heatmap below shows Sharpe Ratio across parameter combinations.

![EMA Heatmap](heatmap.png)

#Key Insights

- Performance varies significantly across parameter space
- No strong, stable high-Sharpe region observed
- Indicates the base EMA crossover lacks persistent edge
- Highlights need for:
  - Volatility filtering
  - Risk management
  - Multi-factor signals

# Interpretation

A robust strategy should exhibit:

- Broad region of positive Sharpe
- Stability across parameter variations

Current results suggest:

> The strategy is sensitive to parameter selection and not yet production-ready.
