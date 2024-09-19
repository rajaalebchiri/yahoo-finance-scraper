# csv_exporter.py

import csv
from config.settings import CSV_FILE_PATH

def export_to_csv(tickers):
    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Ticker', 'Price', 'Company Name',
                        'Volume', 'Open', 'Previous Close', 'Date Time'])
        for ticker in tickers:
            writer.writerow([ticker['ticker'], ticker['price'], ticker['company_name'], ticker['volume'],
                             ticker['open'], ticker['previous_close'], ticker['date_time']])
