# LucraQuant

LucraQuant is a modular, object‑oriented Python backtesting engine that makes it easy to prototype, evaluate, and visualize trading strategies.

## Legal Disclaimer 

Disclaimer
The LucraQuant software and all accompanying files (collectively, the “Software”) are provided solely for educational and informational purposes. By downloading, installing, or using the Software, you acknowledge and agree that:

As-Is / No Warranty – The Software is supplied “AS IS,” without any express or implied warranty of any kind, including but not limited to warranties of merchantability, fitness for a particular purpose, non-infringement, or that the Software will be error-free or operate without interruption.

Use at Your Own Risk – All decisions made with, or based on, the Software are entirely your responsibility. Trading and investing involve substantial risk, and past performance does not guarantee future results.

Limitation of Liability – In no event shall the authors, contributors, or copyright holders be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, loss of profits, trading losses, or business interruption) arising out of or in connection with the use of the Software, even if advised of the possibility of such damages.

Indemnification – You agree to indemnify, defend, and hold harmless the authors and contributors from and against any and all claims, liabilities, losses, damages, costs, or expenses (including reasonable attorneys’ fees) resulting from your use or misuse of the Software.

Compliance – You are solely responsible for ensuring that your use of the Software complies with all applicable laws, regulations, and exchange or broker rules in your jurisdiction.

By proceeding to download or use the Software, you expressly accept all responsibility and liability for any outcomes that may result.

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
