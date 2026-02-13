import yfinance as yf
import pandas as pd
from pathlib import Path


def download(symbol, start, end):
    data = yf.download(symbol, start=start, end=end, auto_adjust=False)

    path = Path("data/raw")
    path.mkdir(parents=True, exist_ok=True)
    data.to_csv(path / f"{symbol}.csv")

def data_clean():
    df = pd.read_csv("data/raw/AAPL.csv")

    print(df.isna().sum())
    print(df.duplicated().sum())
    print(df.head())
    print(df.tail())

if __name__ == "__main__":
    download(symbol="AAPL", start="2010-01-01", end="2025-12-31")
    data_clean()