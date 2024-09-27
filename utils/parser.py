import argparse


def setup_argparse():
    parser = argparse.ArgumentParser(description="Yahoo Finance Scraper")

    # Basic scraping arguments
    parser.add_argument('-t', '--tickers', nargs='+', required=True,
                        help='List of stock ticker symbols to scrape')
    
    parser.add_argument('-pd', '--pandas',
                        help='display as a data frame', action='store_true')
    
    parser.add_argument("--csv", action="store_true",
                        help="Export data to CSV")

    parser.add_argument('--historical', action='store_true',
                        help='Scrape historical data')

    # Historical data options
    parser.add_argument('--start-date', type=str,
                        help='Start date for historical data (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str,
                        help='End date for historical data (YYYY-MM-DD)')



  

    return parser
