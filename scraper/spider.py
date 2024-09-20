# spider.py
import datetime
import requests
from bs4 import BeautifulSoup


def scrape_tickers(tickers):
    """Scrape Tickers, ticker, price, company name, volume, open, previous_close, date time"""
    url = "https://finance.yahoo.com/quote/"
    tickers_data = []
    for ticker in tickers:
        response = requests.get(url + ticker, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')

        live_price_element = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketPrice'})

        company_name = soup.find('h1', class_='yf-vfa1ac').get_text()

        voulume = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketVolume'}).get_text()

        open_data = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketOpen'}).get_text()

        close_data = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketPreviousClose'}).get_text()
        date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M")

        live_price = live_price_element.find('span').get_text()
        tickers_data.append(
            {
                'ticker': ticker,
                'price': live_price,
                'company_name': company_name,
                'volume': voulume,
                'open': open_data,
                'previous_close': close_data,
                'date_time': date_time
            })

    return tickers_data


def scrape_historical_data(tickers, start_date, end_date):
    """Scrape historical data"""
    url = " https://finance.yahoo.com/quote/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    tickers_data = []
    ts_start_date = datetime.datetime.timestamp(
        datetime.datetime.strptime(start_date, "%Y-%m-%d"))
    ts_end_date = datetime.datetime.timestamp(
        datetime.datetime.strptime(end_date, "%Y-%m-%d"))

    for ticker in tickers:
        response = requests.get(
            url=f"{url}{ticker}/history/?period1={int(ts_start_date)}&period2={int(ts_end_date)}",
            headers=headers,
            timeout=5
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        tbody = soup.find('tbody')

        lines = tbody.find_all('tr', class_='yf-ewueuo')
        for line in lines:

            cells = line.find_all('td', class_='yf-ewueuo')

            # Extracting data from each cell
            if len(cells) >= 6:  # Ensure there are enough cells to prevent index errors
                record = {
                    'ticker': ticker,
                    'date': cells[0].get_text(),
                    'open': cells[1].get_text(),
                    'high': cells[2].get_text(),
                    'low': cells[3].get_text(),
                    'close': cells[4].get_text(),
                    'adj_close': cells[5].get_text(),
                    'volume': cells[6].get_text()
                }
                tickers_data.append(record)

    return tickers_data


# data = scrape_historical_data(
#     tickers=['AAPL', 'NVDA', 'MSFT'], start_date='2022-01-01', end_date='2022-12-31')

