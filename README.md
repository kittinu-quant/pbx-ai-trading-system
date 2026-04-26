# pbx-ai-trading-system

## Overview

This project builds a **research-to-production quantitative trading pipeline**, 
designed to discover, validate, and scale alpha strategies across multiple assets.

The focus is not on a single trading strategy, but on constructing a **robust systematic framework** 
for alpha generation, validation, and portfolio deployment.

---

## ⚡ System Positioning

This project demonstrates a **full-stack quantitative trading system**:

- Alpha generation (EMA-based signals)
- Robustness validation (parameter sensitivity + out-of-sample testing)
- Portfolio construction (multi-asset + volatility-adjusted allocation)
- Risk-aware design for scalable deployment

The system represents a **research-to-production pipeline**,  
aimed at developing an **institutional-grade alpha engine**.

---

## Key Results

| Metric | Value |
|------|------|
| Portfolio Sharpe | 0.72 |
| Max Drawdown | -22% |
| Assets | AAPL, BTC, Gold |

---

## Why This Matters

Most simple trading strategies fail due to lack of robustness.

This framework focuses on:

- Avoiding overfitting through validation  
- Ensuring cross-asset consistency  
- Building scalable alpha beyond a single signal  

---

## System Architecture

- **Alpha Engine**  
  Signal generation using EMA-based strategies  

- **Risk Engine**  
  Position sizing and drawdown control  

- **Execution Engine**  
  Backtesting and trade simulation  

- **Portfolio Engine**  
  Multi-asset allocation and optimization  

---

## Strategy Performance

![Equity Curve](equity_curve.png)

| Metric | Value |
|------|------|
| Sharpe | 0.20 |
| Max Drawdown | -35% |

---

## Parameter Optimization (EMA Heatmap)

![EMA Heatmap](heatmap.png)

---

## Research Findings

Key observations from experiments:

- Naive EMA crossover lacks persistent edge  
- Performance varies across assets (BTC > AAPL)  
- High drawdown indicates missing risk control  

---

## Portfolio Construction

### Allocation Method
- Inverse volatility weighting

---

## Portfolio Equity Curve

![Portfolio Equity Curve](Portfolio%20Equity%20Curve.png)

The portfolio demonstrates steady growth with controlled drawdowns.

---

## Portfolio Performance

| Metric | Value |
|------|------|
| Sharpe | 0.72 |
| Max Drawdown | -22% |

---

## Validation & Robustness

### Out-of-Sample Preview

| Asset | In-Sample Sharpe | Out-of-Sample Sharpe |
|------|------------------|---------------------|
| BTC  | 0.62             | 0.38                |
| Gold | 0.44             | 0.31                |

---

## Correlation & Diversification

| Asset | AAPL | BTC | Gold |
|------|------|-----|------|
| AAPL | 1.00 | 0.25 | -0.10 |
| BTC  | 0.25 | 1.00 | 0.05 |
| Gold | -0.10 | 0.05 | 1.00 |

---

## Conclusion

A simple EMA crossover strategy fails to deliver sustainable alpha.

---

## Philosophy

> “We engineer edge, not just trades.”

---

## Author

Kittinu Muayteng
