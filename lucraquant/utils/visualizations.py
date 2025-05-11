import matplotlib.pyplot as plt
import pandas as pd

def plot_equity_curve(equity: pd.Series):
    plt.figure(figsize=(10, 4))
    equity.plot()
    plt.title("Portfolio Value Over Time")
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.tight_layout()
    plt.show()
