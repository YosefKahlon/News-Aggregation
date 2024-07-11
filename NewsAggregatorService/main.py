from fastapi import FastAPI
from aggregator import news_router

app = FastAPI()

app.include_router(news_router, prefix="/news", tags=["news"])

@app.get("/")
def read_root():
    return {"message": "News Aggregator Service is up and running"}
