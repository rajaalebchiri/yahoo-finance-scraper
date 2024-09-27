# main.py
from scraper.spider import scrape_tickers, scrape_historical_data
from database.db_handler import create_table, insert_tickers, create_historical_table, insert_historical_tickers
from export.csv_exporter import export_to_csv
from export.pandas_exporter import export_to_pandas
from utils.logger import setup_logger
from utils.parser import setup_argparse
from data_processing.processor import date_validator, validate_date_range


def process_tickers(args, logger):
    """Processing Tickers"""
    logger.info("Starting the ticker scraping process ...")
    tickers = scrape_tickers(args.tickers)
    logger.info("Fetched %d tickers", len(tickers))
    create_table()
    insert_tickers(tickers)
    logger.info("Inserted tickers into the database")
    logger.info("Scraping process completed")
    return tickers


def process_historical_data(args, logger):
    """Processing historical data"""
    if not validate_historical_args(args, logger):
        return None
    logger.info("Starting the historical data scraping process")
    data = scrape_historical_data(args.tickers, args.start_date, args.end_date)
    logger.info(f"Fetched historical data for {len(data)} tickers")
    create_historical_table()
    insert_historical_tickers(tickers_data=data)
    logger.info("Inserted historical data into the database")

    return data


def validate_historical_args(args, logger):
    """Validate historical data arguments"""
    if not args.start_date or not args.end_date:
        logger.error(
            "Start Date and End Date are required for historical data")
        return False
    if not date_validator(args.start_date) or not date_validator(args.end_date):
        logger.error("Inbalid date format")
        return False
    if args.start_date > args.end_date:
        logger.error("Start Date cannot be greater than End Date")
        return False
    if not validate_date_range(args.start_date, args.end_date):
        return False
    return True


def output_data(data, args, logger):
    """Data output types"""
    if args.csv:
        if args.historical:
            export_to_csv(data, data_type='historical')
        else:
            export_to_csv(data)
        logger.info("Exported data to CSV")
        print("Data exported successfully as finance.csv")
    elif args.pandas:
        df = export_to_pandas(data)
        logger.info("Converted data to Pandas DataFrame")
        print(df)
        logger.info("Exporting data as a CSV with name data.csv")
        print("Data exported successfully as data.csv")
    else:
        logger.info(
            "Data inserted into database. No additional output specified.")


def main():
    """main functions"""
    parser = setup_argparse()
    args = parser.parse_args()
    logger = setup_logger()

    if args.historical:
        data = process_historical_data(args, logger)
    else:
        data = process_tickers(args, logger)

    if data:
        output_data(data, args, logger)
        logger.info("Processing completed successfully")
    else:
        logger.error("No data to process. Please check your inputs and try again")

if __name__ == "__main__":
    main()
