import pandas as pd

class SMACrossoverStrategy:
    def __init__(self, data: pd.DataFrame, short_window: int = 20, long_window: int = 50):
        self.data = data
        self.short_window = short_window
        self.long_window = long_window
        self.prev_signal = 0  # No position

        self.data['sma_short'] = self.data['Close'].rolling(window=self.short_window).mean()
        self.data['sma_long'] = self.data['Close'].rolling(window=self.long_window).mean()

    def generate_signal(self, dt):
        if pd.isna(self.data.loc[dt, 'sma_short']) or pd.isna(self.data.loc[dt, 'sma_long']):
            return None
        if self.data.loc[dt, 'sma_short'] > self.data.loc[dt, 'sma_long'] and self.prev_signal <= 0:
            self.prev_signal = 1
            return 1  # Buy
        elif self.data.loc[dt, 'sma_short'] < self.data.loc[dt, 'sma_long'] and self.prev_signal >= 0:
            self.prev_signal = -1
            return -1  # Sell
        return None
