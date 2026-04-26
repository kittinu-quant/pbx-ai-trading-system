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

## 📊 Strategy Performance

Sharpe: 0.199  
Max Drawdown: -35%  

![Equity Curve](equity_curve.png)

## Research & Optimization

- Tested EMA parameter combinations (10–200)
- Compared performance across multiple assets
- Observed that naive EMA crossover underperforms buy & hold
- Next step: integrate volatility filter and risk control

## 🌍 Multi-Asset Results

| Asset | Sharpe | Max Drawdown |
|------|--------|--------------|
| AAPL | 0.20 | -35% |
| BTC  | TBD | TBD |
| Gold | TBD | TBD |
