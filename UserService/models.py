from pydantic import BaseModel
from typing import List

class User(BaseModel):
    email: str
    name: str

class UserPreferences(BaseModel):
    categories: List[str]
    technologies: List[str]
    communication_channel: str  # Add this line
