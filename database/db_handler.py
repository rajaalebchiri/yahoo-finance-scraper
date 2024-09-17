# db_handler.py

import sqlite3
from config.settings import DB_NAME

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news
        (title TEXT, summary TEXT)
    ''')
    conn.commit()
    conn.close()

def insert_news(news):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO news VALUES (?, ?)', [(article['title'], article['summary']) for article in news])
    conn.commit()
    conn.close()