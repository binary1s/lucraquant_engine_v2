# LucraQuant

LucraQuant is a modular, object‑oriented Python backtesting engine that makes it easy to prototype, evaluate, and visualize trading strategies.

## Features

* SMA crossover, mean reversion, pairs trading, and sentiment‑based strategies out of the box  
* Multi‑asset support with commission and slippage simulation  
* Performance metrics: Total return, annualized return, annualized volatility, Sharpe, Sortino, maximum drawdown  
* Clear visualizations: equity curve, daily returns, drawdown curve, and buy–sell markers  
* Data loading from local CSV files (with a `Close` column) or optionally via the OpenBB SDK  
* Run via a CLI (`run_backtest.py`) or interactively in the included Jupyter notebook

## Requirements

* Python 3.7 or newer  
* virtualenv (recommended)

Install dependencies with:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Installation

```bash
unzip lucraquant_engine_v1.zip
cd lucraquant
```

## Project Structure

```
lucraquant_engine_v1/
    data/               # sample CSV files (you can find more csv files for stocks on nasdaq.com)
    engine/             # core engine logic
    strategies/         # strategy implementations
    utils/              # helper functions and plots
    notebooks/          # Jupyter demos
    run_backtest.py     # CLI entry
    requirements.txt
    README.md
```

## Quick Start (CLI)

```bash
python run_backtest.py --data data/sample.csv \
                       --strategy lucraquant.strategies.my_strategy.SMACrossoverStrategy
```

## Quick Start (Notebook)

Open `notebooks/run_backtest.ipynb` and run the cells.

## Metrics Explained

* **Total Return** – overall percentage gain  
* **Annualized Return** – CAGR adjusted for trading days  
* **Annualized Volatility** – standard deviation of daily returns, annualized  
* **Sharpe Ratio** – risk‑adjusted return relative to volatility  
* **Sortino Ratio** – downside‑risk‑adjusted return  
* **Maximum Drawdown** – largest equity peak‑to‑trough decline

## Visualizations

The `utils.visualizations` module offers helper functions such as `plot_equity_curve`.  
Extend it to add daily returns, drawdown curves, or custom plots.

## Customization

* **New strategies** – add a file in `strategies/` and point the CLI to the class.  
* **Extra metrics** – add a method to `engine/metrics.py`.  
* **Additional plots** – create functions in `utils/visualizations.py`.

## Troubleshooting

* **Missing Close column** – ensure your CSV has `Close` prices and a datetime index.  
* **No trades generated** – verify strategy parameters generate buy/sell signals.  
* **Matplotlib display issues** – run the notebook with `%matplotlib inline`.

## License

MIT License – see `LICENSE` file (coming soon).

## Support

Open an issue or email the maintainer at vehbi@lucraquant.com