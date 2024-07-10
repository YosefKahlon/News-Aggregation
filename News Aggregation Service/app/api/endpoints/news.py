# This file defines the API endpoints related to news.
# news_aggregation_service/app/api/endpoints/news.py


from fastapi import APIRouter, HTTPException
from app.services.news_service import fetch_news
from app.models.news import NewsResponse

router = APIRouter()

@router.get("/", response_model=NewsResponse)
def get_news(query: str):
    try:
        news = fetch_news(query)
        return news
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
