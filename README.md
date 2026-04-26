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

The system demonstrates improved robustness through:

- Multi-asset diversification  
- Volatility-aware filtering  
- Portfolio-level optimization  

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

## Research Findings

Key observations from experiments:

- Naive EMA crossover lacks persistent edge  
- Performance varies across assets (BTC > AAPL)  
- High drawdown indicates missing risk control  

Implications:

- Strategy requires volatility filtering  
- Position sizing is critical  
- Multi-factor signals are needed  

---

## Portfolio Construction

### Allocation Method
- Inverse volatility weighting

Formula:

w_i = (1 / σ_i) / Σ(1 / σ_i)

Where:
- σ_i = volatility of asset i

This approach:
- Reduces exposure to high-volatility assets (e.g., BTC)
- Improves portfolio stability

---

## Portfolio Equity Curve

![Portfolio Equity Curve](Portfolio%20Equity%20Curve.png)

The portfolio demonstrates steady growth with controlled drawdowns,  
highlighting the benefit of diversification and risk-aware allocation.

---

## Portfolio Performance

| Metric | Value |
|------|------|
| Sharpe | 0.72 |
| Max Drawdown | -22% |

---

## Validation & Robustness

Validation steps performed:

- Parameter sensitivity analysis (EMA heatmap)
- Multi-asset testing (AAPL, BTC, Gold)
- Preliminary out-of-sample testing

### Out-of-Sample Preview

| Asset | In-Sample Sharpe | Out-of-Sample Sharpe |
|------|------------------|---------------------|
| BTC  | 0.62             | 0.38                |
| Gold | 0.44             | 0.31                |

Observation:

- Performance degrades but remains positive  
- Indicates partial robustness  
- Suggests volatility filtering improves generalization  

---

## Correlation & Diversification

### Correlation Matrix

| Asset | AAPL | BTC | Gold |
|------|------|-----|------|
| AAPL | 1.00 | 0.25 | -0.10 |
| BTC  | 0.25 | 1.00 | 0.05 |
| Gold | -0.10 | 0.05 | 1.00 |

Insight:

- Low correlation improves diversification  
- Portfolio-level construction enhances risk-adjusted return  

---

## Conclusion

A simple EMA crossover strategy fails to deliver sustainable alpha.

Robust performance requires:

- Regime filtering  
- Risk-adjusted allocation  
- Multi-asset diversification  

This project demonstrates the transition from:

> "Single-indicator strategy" → "Systematic alpha framework"

---

## Next Steps

To move toward production-grade deployment:

- Multi-factor signal integration  
- Regime-based filtering (ATR, ADX)  
- Risk parity / volatility targeting  
- Portfolio-level Sharpe optimization  
- Walk-forward validation  
- Transaction cost & slippage modeling  

---

## Philosophy

> “We engineer edge, not just trades.”

---

## Author

Kittinu Muayteng
