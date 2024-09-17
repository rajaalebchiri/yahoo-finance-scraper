# main.py
from scraper.spider import fetch_news
from database.db_handler import create_table, insert_news
from export.csv_exporter import export_to_csv
from utils.logger import setup_logger
import argparse

def main():
    parser = argparse.ArgumentParser(description="CSV Scraping Export")
    parser.add_argument("--csv", action="store_true", help="Export data to CSV")
    args = parser.parse_args()
    
    logger = setup_logger()
    logger.info("Starting the scraping process")
    
    create_table()
    
    news = fetch_news()
    logger.info(f"Fetched {len(news)} news")
    
    insert_news(news)
    logger.info("Inserted books into the database")
    
    if args.csv:
        export_to_csv(news)
        logger.info("Exported news to CSV")
    
    logger.info("Scraping process completed")
    
if __name__ == "__main__":
    main()