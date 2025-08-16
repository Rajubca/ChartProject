import requests
import pandas as pd
from io import StringIO


def fetch_nifty_dataframe():
    url = (
        "https://www.nseindia.com/api/equity-stockIndices"
        "?csv=true&index=NIFTY%2050&selectValFormat=crores"
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/market-data/live-equity-market",
    }

    with requests.Session() as session:
        session.get("https://www.nseindia.com/market-data/live-equity-market", headers=headers)
        response = session.get(url, headers=headers)
        response.raise_for_status()

    df = pd.read_csv(StringIO(response.text))
    return df


if __name__ == "__main__":
    df = fetch_nifty_dataframe()
    print(df.head())
