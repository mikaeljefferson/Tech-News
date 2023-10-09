import requests
import time
from bs4 import BeautifulSoup


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
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
