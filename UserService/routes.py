import os
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, Body
from models import User, UserPreferences
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

if not mongo_uri:
    raise ValueError("MONGODB_URI environment variable not set")

client = MongoClient(mongo_uri)
db = client.news_db
user_collection = db.users

user_router = APIRouter()

@user_router.post("/register")
async def register_user(user: User):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already registered")
    user_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@user_router.post("/preferences")
async def set_preferences(email: str = Body(...), preferences: UserPreferences = Body(...)):
    user = user_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_collection.update_one({"email": email}, {"$set": {"preferences": preferences.dict()}})
    return {"message": "Preferences updated successfully"}

@user_router.get("/status")
async def get_status():
    return {"message": "User Service is running"}
