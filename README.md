# Yahoo Financial Scraper

## Overview

This project is a Python-based web scraper designed to extract useful financial data from yahoo finance website. It demonstrates a modular approach to web scraping, data processing, and storage, with the added capability of exporting data to CSV format.

URL: https://finance.yahoo.com/

## Features

- Scrape financial data for multiple stocks using ticker symbols
- Store scraped data in a SQLite database
- Option to export data as a CSV file
- Option to display and export data as a pandas DataFrame
- Logging functionality for tracking the scraping process
- Command-line interface for easy usage

## Project Structure

```
yahoo_finance_scraper/
│
├── scraper/
│   ├── __init__.py
│   └── spider.py
│
├── data_processing/
│   ├── __init__.py
│   └── processor.py
│
├── database/
│   ├── __init__.py
│   └── db_handler.py
│
├── export/
│   ├── __init__.py
│   └── csv_exporter.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│   └── parser.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/yahoo-finance-scraper.git
   cd yahoo-finance-scraper
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the scraper:

```
python main.py --tickers AAPL GOOGL MSFT [options]
```

### Command-line Options

- `--tickers`: List of stock ticker symbols to scrape (required)
- `--pandas`: Display data as a pandas DataFrame and export to 'data.csv'
- `--csv`: Export data to 'finance.csv'

### Examples

1. Scrape data and store in SQLite database:
   ```
   python main.py --tickers AAPL GOOGL MSFT
   ```

2. Scrape data, display as pandas DataFrame, and export to 'data.csv':
   ```
   python main.py --tickers AAPL GOOGL MSFT --pandas
   ```

3. Scrape data and export to 'finance.csv':
   ```
   python main.py --tickers AAPL GOOGL MSFT --csv
   ```

## Output

1. SQLite database: All scraped data is stored in a SQLite database (table and database details to be specified).

2. Console output: If the `--pandas` option is used, the scraped data will be displayed in the console as a pandas DataFrame.

3. CSV files:
   - If the `--pandas` option is used, printed as df and data will be exported to 'data.csv'.
   - If the `--csv` option is used, data will be exported to 'finance.csv'.

## Configuration

You can modify the following settings in `config/settings.py`:

- `DB_NAME`: Name of the SQLite database file
- `LOG_FILE`: Name of the log file
- `CSV_FILE_PATH`: Path and name of the CSV file (when using the CSV export option)

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Wikipedia for providing the current events page
- The open-source community for the excellent Python libraries used in this project