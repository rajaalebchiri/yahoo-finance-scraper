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
