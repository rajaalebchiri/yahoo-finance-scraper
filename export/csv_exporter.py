# csv_exporter.py

import csv
from config.settings import CSV_FILE_PATH

def export_to_csv(news):
    with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['title', 'summary']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for article in news:
            writer.writerow(article)