# main.py
from scraper.spider import scrape_tickers
from database.db_handler import create_table, insert_tickers
from export.csv_exporter import export_to_csv
from export.pandas_exporter import export_to_pandas
from utils.logger import setup_logger
from utils.parser import setup_argparse


def main():

    parser = setup_argparse()

    args = parser.parse_args()

    logger = setup_logger()
    logger.info("Starting the scraping process")

    tickers = scrape_tickers(args.tickers)
    logger.info(f"Fetched {len(tickers)} tickers")
    
    create_table()

    insert_tickers(tickers)
    logger.info("Inserted tickers into the database")

    if args.pandas:
        df = export_to_pandas(tickers)
        logger.info("Printing tickers informations as a Pandas DataFrame")
        print(df)
        logger.info("Exporting tickers informations as a CSV with name data.csv")
        print("Data exported successfully as data.csv")
    elif args.csv:
        export_to_csv(tickers)
        logger.info("Exported financial data to CSV")
        print("Data exported successfully as finance.csv")

    
    logger.info("Scraping process completed")


if __name__ == "__main__":
    main()
