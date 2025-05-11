import pandas as pd
from typing import Type, Dict, Any
from .portfolio import Portfolio
from .metrics import Metrics

class BacktestEngine:
    """Simple event driven backtest engine."""

    def __init__(self,
                 data: pd.DataFrame,
                 strategy_cls: Type,
                 initial_capital: float = 10000.0,
                 commission: float = 0.0,
                 slippage: float = 0.0,
                 strategy_kwargs: Dict[str, Any] | None = None):
        self.data = data
        self.strategy = strategy_cls(data, **(strategy_kwargs or {}))
        self.portfolio = Portfolio(initial_capital, commission, slippage)

    def run(self) -> Dict[str, Any]:
        for dt, row in self.data.iterrows():
            price = row['Close']
            signal = self.strategy.generate_signal(dt)
            if signal is not None:
                self.portfolio.execute_signal(signal, price, dt)
            self.portfolio.update_market_value(price, dt)
        # Close any open positions at final price
        final_price = self.data.iloc[-1]['Close']
        self.portfolio.close_all_positions(final_price, self.data.index[-1])
        metrics = Metrics.calculate(self.portfolio.equity_curve)
        return {
            "portfolio_values": self.portfolio.equity_curve,
            "metrics": metrics,
            "trades": self.portfolio.trades
        }
