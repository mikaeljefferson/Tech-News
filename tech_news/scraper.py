import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news


# Requisito 1
def fetch(URL: str):
    """Seu código deve vir aqui"""
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        res = requests.get(URL, headers=headers, timeout=3)
        if res.status_code == 200:
            return res.text
        return None

    except requests.Timeout:
        return None
    except Exception as e:
        print(e)
        return None


# Requisito 2
def scrape_updates(html_content: str) -> list:
    """Seu código deve vir aqui"""
    soup = BeautifulSoup(html_content, "html.parser")
    result = []
    for quote in soup.find_all("header", {"class": "entry-header"}):
        tag = quote.h2.a["href"]
        result.append(tag)

    return result


# Requisito 3
def scrape_next_page_link(html_content: str) -> str:
    """Seu código deve vir aqui"""
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", {"class": "next page-numbers"})
    if next_page:
        return next_page["href"]
    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    soup = BeautifulSoup(html_content, 'html.parser')
    data_news = {}

    url = soup.find('link', {'rel': 'canonical'})
    data_news['url'] = url['href']

    title = soup.find('h1', class_='entry-title')
    data_news['title'] = title.get_text().strip()

    timestamp = soup.find('li', class_='meta-date')
    data_news['timestamp'] = timestamp.get_text()

    writer = soup.find("span", class_="author")
    data_news['writer'] = writer.get_text().strip()

    reading_time = soup.find('li', class_='meta-reading-time')
    reading_time_text = reading_time.get_text().strip()
    data_news['reading_time'] = int(reading_time_text.split()[0])

    summary = soup.find_all('p')[:1]
    summary_text = ''.join([element.get_text() for element in summary]).strip()
    data_news['summary'] = summary_text

    category = soup.find('span', class_='label')
    data_news['category'] = category.get_text()

    return data_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = 'https://blog.betrybe.com/'
    all_news = []

    while len(all_news) < amount:
        content = fetch(url)
        next_page = scrape_next_page_link(content)
        news_links = scrape_updates(content)
        all_news.extend([scrape_news(fetch(link)) for link in news_links])
        url = next_page

    all_news = all_news[:amount]

    create_news(all_news)

    return all_news
