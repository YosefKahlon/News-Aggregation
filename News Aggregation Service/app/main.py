# from fastapi import FastAPI, HTTPException, Query
# from newsdataapi import NewsDataApiClient
#
# app = FastAPI()
#
# # Initialize the Newsdata.io client with your API key
# api = NewsDataApiClient(apikey="pub_48063cce1accd09a0abf083d080547aa4b104")
#
# @app.get("/news/")
# async def get_news(q: str = Query(None, description="Search query for news"), country: str = Query(None, description="Country code for news"), language: str = Query('en', description="Language code for news")):
#     try:
#         # Fetch news data from Newsdata.io
#         response = api.news_api(q=q, country=country, language=language)
#         # Return the response
#         return response
#     except Exception as e:
#         # Handle errors and return an appropriate response
#         raise HTTPException(status_code=500, detail=str(e))
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
