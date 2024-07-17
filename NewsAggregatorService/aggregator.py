from fastapi import APIRouter, HTTPException
import requests
import os
import google.generativeai as genai
import logging

news_router = APIRouter()

NEWS_API_URL = "https://newsdata.io/api/1/news?category="
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

logging.basicConfig(level=logging.INFO)

@news_router.get("/fetch")
async def fetch_news(category: str):
    """Fetch news articles by category"""
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        logging.error("API key for news data not found")
        raise HTTPException(status_code=500, detail="API key for news data not found")

    response = requests.get(f"{NEWS_API_URL}{category}&apikey={api_key}")
    if response.status_code != 200:
        logging.error("Failed to fetch news: %s", response.text)
        raise HTTPException(status_code=500, detail="Failed to fetch news")
    return response.json()

@news_router.get("/summarize")
async def summarize_news(category: str):
    """Fetch and summarize news articles by category"""
    news_response = await fetch_news(category)
    articles = news_response.get("results", [])

    if not articles:
        raise HTTPException(status_code=404, detail="No news articles found")

    summaries = []
    for article in articles:
        summary = get_summary(article["description"])
        summaries.append({
            "title": article["title"],
            "summary": summary,
            "url": article["link"]
        })

    return {"category": category, "summaries": summaries}

def get_summary(text: str) -> str:
    """Get summary of the text using AI"""
    try:
        response = model.generate_content(f"Summarize the following text: {text}")
        summary = response.text.strip()
        return summary
    except Exception as e:
        logging.error("Failed to get summary from AI service: %s", str(e))
        raise HTTPException(status_code=500, detail="Failed to get summary from AI service")