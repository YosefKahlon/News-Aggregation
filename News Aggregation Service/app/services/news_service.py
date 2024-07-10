# news_aggregation_service/app/services/news_service.py

import requests
from app.core.config import settings
from app.models.news import NewsResponse

def fetch_news(query: str):
    url = f"https://newsdata.io/api/1/news?apikey={settings.NEWS_API_KEY}&q={query}"
    response = requests.get(url)
    response.raise_for_status()
    return NewsResponse(**response.json())
