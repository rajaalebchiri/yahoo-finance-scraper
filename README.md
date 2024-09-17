# Wikipedia News Scraper

## Overview

This project is a Python-based web scraper designed to extract the latest news headlines from Wikipedia's current news page. It demonstrates a modular approach to web scraping, data processing, and storage, with the added capability of exporting data to CSV format.

URL: https://en.wikinews.org/wiki/Main_Page

## Features

- Scrapes news headlines and summaries from Wikipedia's current news page
- Stores the data in a SQLite database
- Offers an option to export data to CSV format
- Implements logging for better tracking and debugging

## Project Structure

```
wikipedia_news_scraper/
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
│
├── main.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/wikipedia-news-scraper.git
   cd wikipedia-news-scraper
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

1. To run the scraper and store data in the database:
   ```
   python main.py
   ```

2. To run the scraper, store data in the database, and generate a CSV file:
   ```
   python main.py --csv
   ```

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