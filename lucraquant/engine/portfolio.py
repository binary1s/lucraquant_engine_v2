import pandas as pd
from datetime import datetime
from typing import List, Dict

class Portfolio:
    def __init__(self, initial_capital: float, commission: float, slippage: float):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.position = 0  # number of shares
        self.trades: List[Dict] = []
        self.commission = commission
        self.slippage = slippage
        self.equity_curve = pd.Series(dtype=float)

    def execute_signal(self, signal: int, price: float, dt: datetime):
        # signal: 1 = buy, -1 = sell/close
        if signal == 1 and self.cash > 0:
            # buy as many shares as possible
            quantity = self.cash // price
            if quantity <= 0:
                return
            cost = quantity * price * (1 + self.slippage) + self.commission
            self.cash -= cost
            self.position += quantity
            self.trades.append({"type": "BUY", "dt": dt, "qty": quantity, "price": price})
        elif signal == -1 and self.position > 0:
            proceeds = self.position * price * (1 - self.slippage) - self.commission
            self.cash += proceeds
            self.trades.append({"type": "SELL", "dt": dt, "qty": self.position, "price": price})
            self.position = 0

    def update_market_value(self, price: float, dt: datetime):
        equity = self.cash + self.position * price
        self.equity_curve.loc[dt] = equity

    def close_all_positions(self, price: float, dt: datetime):
        if self.position > 0:
            proceeds = self.position * price - self.commission
            self.cash += proceeds
            self.trades.append({"type": "SELL", "dt": dt, "qty": self.position, "price": price})
            self.position = 0
        # final equity update
        self.update_market_value(price, dt)
