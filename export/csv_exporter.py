# csv_exporter.py

import csv
from config.settings import CSV_FILE_PATH
from typing import List, Dict


def export_to_csv(data: List[Dict[str, str]], file_path: str = CSV_FILE_PATH, data_type: str = 'tickers'):
    """Export data to a CSV file

    :param data: List of dictionaries containing the data to export
    :param file_path: Path where the CSV file will be saved
    :param data_type: Type of data being exported ('tickers' or 'historical')
    """
    if not data:
        print("No data to export")
        return

    if data_type == 'tickers':
        headers = ['Ticker', 'Price', 'Company Name', 'Volume', 'Open', 'Previous Close', 'Date Time']
        row_data = lambda item: [
            item['ticker'], item['price'], item['company_name'], item['volume'],
            item['open'], item['previous_close'], item['date_time']
        ]
    elif data_type == 'historical':
        headers = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        row_data = lambda item: [
            item['ticker'], item['date'], item['open'], item['high'], item['low'],
            item['close'], item['adj_close'], item['volume']
        ]
    else:
        raise ValueError(
            "Invalid data_type. Must be 'tickers' or 'historical'.")

    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for item in data:
                writer.writerow(row_data(item))
        print(f"Data exported successfully to {file_path}")
    except Exception as e:
        print(f"Error exporting data to CSV: {str(e)}")
