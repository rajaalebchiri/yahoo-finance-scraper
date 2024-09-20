# db_handler.py

import sqlite3
from config.settings import DB_NAME


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_data (
    ticker VARCHAR(10),
    price DECIMAL(10, 2),
    company_name VARCHAR(255),
    volume BIGINT,
    open DECIMAL(10, 2),
    previous_close DECIMAL(10, 2),
    date_time VARCHAR(16)
)
    ''')
    conn.commit()
    conn.close()


def insert_tickers(tickers):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO stock_data VALUES (?, ?, ?, ?, ?, ?, ?)', [
                       (ticker['ticker'], ticker['price'], ticker['company_name'], ticker['volume'],
                        ticker['open'], ticker['previous_close'], ticker['date_time']) for ticker in tickers])
    conn.commit()
    conn.close()


def create_historical_table():
    """Creates the stock_data table if it does not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historical_data (
            ticker VARCHAR(10),
            date VARCHAR(16),
            open DECIMAL(10, 2),
            high DECIMAL(10, 2),
            low DECIMAL(10, 2),
            close DECIMAL(10, 2),
            adj_close DECIMAL(10, 2),
            volume BIGINT
        )
    ''')
    conn.commit()
    conn.close()


def insert_historical_tickers(tickers_data):
    """Inserts historical stock data into the stock_data table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Prepare the SQL statement for insertion
    cursor.executemany('''
        INSERT INTO historical_data (ticker, date, open, high, low, close, adj_close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        (
            ticker['ticker'],
            ticker['date'],
            float(ticker['open'].replace(',', '')),
            float(ticker['high'].replace(',', '')),
            float(ticker['low'].replace(',', '')),
            float(ticker['close'].replace(',', '')),
            float(ticker['adj_close'].replace(',', '')),
            int(ticker['volume'].replace(',', ''))
        )
        for ticker in tickers_data
    ])

    conn.commit()
    conn.close()
