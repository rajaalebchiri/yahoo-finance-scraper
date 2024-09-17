# spider.py
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

fetch_news()