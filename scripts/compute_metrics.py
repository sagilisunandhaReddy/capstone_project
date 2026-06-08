import numpy as np

def calculate_cagr(start_nav, end_nav, years):
    return ((end_nav / start_nav) ** (1 / years)) - 1

def calculate_volatility(returns):
    return returns.std() * np.sqrt(252)

def calculate_sharpe_ratio(returns, risk_free_rate=0.06):
    excess_return = returns.mean() - risk_free_rate / 252
    return (excess_return / returns.std()) * np.sqrt(252)

def calculate_max_drawdown(cumulative_returns):
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown.min()