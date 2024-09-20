# main.py
from scraper.spider import scrape_tickers, scrape_historical_data
from database.db_handler import create_table, insert_tickers, create_historical_table, insert_historical_tickers
from export.csv_exporter import export_to_csv
from export.pandas_exporter import export_to_pandas
from utils.logger import setup_logger
from utils.parser import setup_argparse
from data_processing.processor import date_validator, validate_date_range


def main():

    parser = setup_argparse()

    args = parser.parse_args()

    # turn it into --output
    if args.pandas:
        logger = setup_logger()
        logger.info("Starting the scraping process")

        tickers = scrape_tickers(args.tickers)
        logger.info("Fetched %d tickers", len(tickers))

        create_table()

        insert_tickers(tickers)
        logger.info("Inserted tickers into the database")
        logger.info("Scraping process completed")
        df = export_to_pandas(tickers)
        logger.info("Printing tickers informations as a Pandas DataFrame")
        print(df)
        logger.info(
            "Exporting tickers informations as a CSV with name data.csv")
        print("Data exported successfully as data.csv")
    # turn it into --output
    elif args.csv:
        logger = setup_logger()
        logger.info("Starting the scraping process")

        tickers = scrape_tickers(args.tickers)
        logger.info("Fetched %d tickers", len(tickers))

        create_table()

        insert_tickers(tickers)
        logger.info("Inserted tickers into the database")
        logger.info("Scraping process completed")
        export_to_csv(tickers)
        logger.info("Exported financial data to CSV")
        print("Data exported successfully as finance.csv")
    elif args.historical:
        if not args.start_date or not args.end_date:
            logger.error(
                "Start Date and End Date are required for historical data")
            parser.error("--historical requires --start-date and --end-date")
        elif not date_validator(args.start_date) or not date_validator(args.end_date):
            return
        elif args.start_date > args.end_date:
            logger.error("Start Date must be before End Date")
            parser.error("Start Date must be before End Date")
        elif not validate_date_range(args.start_date, args.end_date):
            return

        logger = setup_logger()
        logger.info("Starting the scraping process")
        data =scrape_historical_data(args.tickers, args.start_date, args.end_date)
        logger.info("Fetched %d historical data", len(data))
        
        create_historical_table()
        
        insert_historical_tickers(tickers_data = data)
        logger.info("Inserted historical data into the database")
        logger.info("Scraping process completed")
    
    logger = setup_logger()
    logger.info("Starting the scraping process")

    tickers = scrape_tickers(args.tickers)
    logger.info("Fetched %d tickers", len(tickers))

    create_table()

    insert_tickers(tickers)
    logger.info("Inserted tickers into the database")
    logger.info("Scraping process completed")


if __name__ == "__main__":
    main()
