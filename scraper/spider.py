# spider.py
import datetime
import requests
from bs4 import BeautifulSoup


def fetch_news():
    url = "https://en.wikinews.org/wiki/Main_Page"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    news = []
    for article in soup.find_all('td', class_='l_box'):
        title = article.find('span', class_='l_title').a.get_text()
        summary = article.find('span', class_='l_summary').get_text()
        news.append({'title': title, 'summary': summary})
    return news


def scrape_tickers(tickers):
    url = "https://finance.yahoo.com/quote/"
    tickers_data = []
    for ticker in tickers:
        response = requests.get(url + ticker)
        soup = BeautifulSoup(response.content, 'html.parser')

        live_price_element = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketPrice'})

        company_name = soup.find('h1', class_='yf-vfa1ac').get_text()

        voulume = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketVolume'}).get_text()

        open = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketOpen'}).get_text()

        close = soup.find(
            'fin-streamer', {'data-symbol': ticker, 'data-field': 'regularMarketPreviousClose'}).get_text()
        date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M")

        live_price = live_price_element.find('span').get_text()
        tickers_data.append(
            {
                'ticker': ticker,
                'price': live_price,
                'company_name': company_name,
                'volume': voulume,
                'open': open,
                'previous_close': close,
                'date_time': date_time
            })

    return tickers_data
