from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    result = db.news.find({"title": {"$regex": title, "$options": "i"}})

    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date_str = date_obj.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    results = db.news.find({"timestamp": {"$regex": f"^{date_str}"}})
    return [(news["title"], news["url"]) for news in results]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    results = db.news.find()
    filtered_results = filter(
        lambda news: category.lower() in news['category'].lower(), results
    )
    return [(news["title"], news["url"]) for news in filtered_results]
