# This file defines the data models for news articles.


from pydantic import BaseModel
from typing import List, Optional


class NewsArticle(BaseModel):
    title: str
    description: Optional[str]
    url: str
    source: str


class NewsResponse(BaseModel):
    status: str
    totalResults: int
    articles: List[NewsArticle]
