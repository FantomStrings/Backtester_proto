import yfinance as yf
from pathlib import Path


def download(symbol, start, end):
    data = yf.download(symbol, start=start, end=end, auto_adjust=False)

    path = Path("data/raw")
    path.mkdir(parents=True, exist_ok=True)
    data.to_csv(path / f"{symbol}.csv")



if __name__ == "__main__":
    download(symbol="AAPL", start="2020-01-01", end="2024-12-31")