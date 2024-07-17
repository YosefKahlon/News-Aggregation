import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Body, Query
from pydantic import BaseModel
from models import User, UserPreferences
from pymongo import MongoClient
import requests
from bson import ObjectId
from aiocache import cached

# Load environment variables from .env file
load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

if not mongo_uri:
    raise ValueError("MONGODB_URI environment variable not set")

client = MongoClient(mongo_uri)
db = client.news_db
user_collection = db.users


class NotifyRequest(BaseModel):
    email: str


class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    preferences: UserPreferences = None


user_router = APIRouter()


@user_router.post("/register")
async def register_user(user: User):
    """Register a new user"""
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already registered")
    user_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}


@user_router.post("/preferences")
async def set_preferences(email: str = Body(...), preferences: UserPreferences = Body(...)):
    """Set user preferences"""
    user = user_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_collection.update_one({"email": email}, {"$set": {"preferences": preferences.dict()}})
    return {"message": "Preferences updated successfully"}


@user_router.get("/status")
@cached(ttl=60)  # Cache for 60 seconds
async def get_status():
    """Check the status of the User Service"""
    return {"message": "User Service is running"}


@user_router.post("/notify")
async def notify_user(request: NotifyRequest):
    """Notify user based on preferences"""
    email = request.email
    user = user_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    preferences = user.get("preferences", {})
    if not preferences:
        raise HTTPException(status_code=400, detail="User preferences not set")

    categories = preferences.get("categories", [])
    technologies = preferences.get("technologies", [])
    communication_channel = preferences.get("communication_channel")

    if not categories and not technologies:
        raise HTTPException(status_code=400, detail="No categories or technologies specified in preferences")

    # Fetch news based on preferences
    summaries = []
    for category in categories:
        response = requests.get(f"http://news-aggregator-service:8001/news/summarize?category={category}")
        if response.status_code == 200:
            summaries.extend(response.json().get("summaries", []))

    # Send the notification
    if communication_channel == "email":
        notify_via_email(email, summaries)
    else:
        raise HTTPException(status_code=400, detail="Unsupported communication channel")

    return {"message": f"Notification sent to {email}"}


def notify_via_email(email, summaries):
    """Send email notification"""
    subject = "Your Personalized News Summary"
    message = "\n\n".join(
        [f"Title: {summary['title']}\nSummary: {summary['summary']}\nURL: {summary['url']}" for summary in summaries])
    data = {
        "email": email,
        "subject": subject,
        "message": message
    }
    response = requests.post("http://notification-service:8002/notify/send", json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to send email notification")


@user_router.delete("/delete")
async def delete_user(email: str = Query(...)):
    """Delete a user"""
    result = user_collection.delete_one({"email": email})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


@user_router.get("/get")
@cached(ttl=60)  # Cache for 60 seconds
async def get_user(email: str = Query(...)):
    """Retrieve user details"""
    user = user_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["_id"] = str(user["_id"])
    return {"user": user}
