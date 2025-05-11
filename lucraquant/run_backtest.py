#!/usr/bin/env python
import argparse, sys, os
import importlib
import pandas as pd
from lucraquant.engine.backtest_engine import BacktestEngine
from lucraquant.engine.data_handler import DataHandler

def main():
    parser = argparse.ArgumentParser(description="Run LucraQuant backtest")
    parser.add_argument("--data", required=True, help="Path to CSV file")
    parser.add_argument("--strategy", default="lucraquant.strategies.my_strategy.SMACrossoverStrategy",
                        help="Strategy class path")
    parser.add_argument("--capital", type=float, default=10000, help="Initial capital")
    parser.add_argument("--commission", type=float, default=0.0, help="Commission per trade")
    parser.add_argument("--slippage", type=float, default=0.0, help="Slippage percentage")
    args = parser.parse_args()

    module_path, cls_name = args.strategy.rsplit(".", 1)
    module = importlib.import_module(module_path)
    strategy_cls = getattr(module, cls_name)

    data = DataHandler.load_csv(args.data)
    engine = BacktestEngine(data, strategy_cls, initial_capital=args.capital,
                            commission=args.commission, slippage=args.slippage)
    results = engine.run()
    print("Backtest complete. Metrics:")
    for k, v in results['metrics'].items():
        print(f"{k}: {v:.4f}")

if __name__ == "__main__":
    main()
