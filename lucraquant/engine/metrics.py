import pandas as pd
import numpy as np

class Metrics:
    @staticmethod
    def calculate(equity_curve: pd.Series, risk_free_rate: float = 0.0):
        returns = equity_curve.pct_change().dropna()
        total_return = (equity_curve.iloc[-1] / equity_curve.iloc[0]) - 1
        ann_return = np.power((1 + total_return), 252 / len(returns)) - 1
        ann_vol = returns.std() * np.sqrt(252)
        sharpe = (ann_return - risk_free_rate) / ann_vol if ann_vol != 0 else 0.0
        downside = returns[returns < 0]
        sortino = (ann_return - risk_free_rate) / (downside.std() * np.sqrt(252)) if not downside.empty else 0.0
        running_max = equity_curve.cummax()
        drawdown = (equity_curve / running_max) - 1
        max_dd = drawdown.min()
        return {
            "Total Return": total_return,
            "Annualized Return": ann_return,
            "Annualized Volatility": ann_vol,
            "Sharpe Ratio": sharpe,
            "Sortino Ratio": sortino,
            "Maximum Drawdown": max_dd
        }
