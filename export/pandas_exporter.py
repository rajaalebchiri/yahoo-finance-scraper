# csv_exporter.py

import pandas as pd


def export_to_pandas(tickers):
    df = pd.DataFrame(tickers)
    df.index += 1
    df.to_csv("data.csv")
    return df
