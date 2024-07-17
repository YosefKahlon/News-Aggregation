from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

USER_SERVICE_URL = "http://user_service:8000/users"
NEWS_SERVICE_URL = "http://news_aggregator_service:8001/news"
NOTIFY_SERVICE_URL = "http://notification_service:8002/notify"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, email: str = Form(...), name: str = Form(...)):
    response = requests.post(f"{USER_SERVICE_URL}/register", json={"email": email, "name": name})
    if response.status_code == 200:
        message = response.json().get("message", "User registered successfully")
        return templates.TemplateResponse("index.html", {"request": request, "message": message})
    else:
        error = response.json().get("detail", "An error occurred")
        return templates.TemplateResponse("index.html", {"request": request, "error": error})

@app.post("/preferences", response_class=HTMLResponse)
async def set_preferences(request: Request, email: str = Form(...), categories: str = Form(...), technologies: str = Form(...), communication_channel: str = Form(...)):
    preferences = {
        "categories": categories.split(","),
        "technologies": technologies.split(","),
        "communication_channel": communication_channel
    }
    response = requests.post(f"{USER_SERVICE_URL}/preferences", json={"email": email, "preferences": preferences})
    if response.status_code == 200:
        message = response.json().get("message", "Preferences updated successfully")
        return templates.TemplateResponse("index.html", {"request": request, "message": message})
    else:
        error = response.json().get("detail", "An error occurred")
        return templates.TemplateResponse("index.html", {"request": request, "error": error})

@app.post("/notify", response_class=HTMLResponse)
async def notify(request: Request, email: str = Form(...)):
    response = requests.post(f"{USER_SERVICE_URL}/notify", json={"email": email})
    if response.status_code == 200:
        message = response.json().get("message", "Notification sent successfully")
        return templates.TemplateResponse("index.html", {"request": request, "message": message})
    else:
        error
