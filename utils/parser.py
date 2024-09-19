import argparse


def setup_argparse():
    parser = argparse.ArgumentParser(description="Yahoo Finance Scraper")

    # Basic scraping arguments
    parser.add_argument('-t', '--tickers', nargs='+', required=True,
                        help='List of stock ticker symbols to scrape')
    # parser.add_argument('-o', '--output', choices=['db', 'csv', 'both'], default='db',
    #                     help='Output format: database, CSV, or both (default: db)')
    
    parser.add_argument('-pd', '--pandas',
                        help='display as a data frame', action='store_true')
    
    parser.add_argument("--csv", action="store_true",
                        help="Export data to CSV")

    # Data type selection
    parser.add_argument('--realtime', action='store_true',
                        help='Scrape real-time data instead of end-of-day data')
    parser.add_argument('--historical', action='store_true',
                        help='Scrape historical data')

    # Historical data options
    parser.add_argument('--start-date', type=str,
                        help='Start date for historical data (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str,
                        help='End date for historical data (YYYY-MM-DD)')

    # Data update options
    parser.add_argument('--update', action='store_true',
                        help='Update existing data for tracked stocks')

    # Specific data points
    parser.add_argument('--price-only', action='store_true',
                        help='Scrape only price-related data')
    parser.add_argument('--financials', action='store_true',
                        help='Scrape detailed financial metrics')
    parser.add_argument('--analyst', action='store_true',
                        help='Scrape analyst recommendations and price targets')

    # Output customization
    parser.add_argument('--csv-file', type=str, default='yahoo_finance_data.csv',
                        help='Name of the CSV file for output (default: yahoo_finance_data.csv)')
    parser.add_argument('--db-name', type=str, default='yahoo_finance.db',
                        help='Name of the SQLite database file (default: yahoo_finance.db)')

    # Scraping behavior
    parser.add_argument('--frequency', type=int, default=5,
                        help='Scraping frequency in seconds (default: 5)')
    parser.add_argument('--max-retries', type=int, default=3,
                        help='Maximum number of retries for failed requests (default: 3)')

    # Logging options
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='INFO', help='Set the logging level')
    parser.add_argument('--log-file', type=str, help='Log file path')

    return parser
