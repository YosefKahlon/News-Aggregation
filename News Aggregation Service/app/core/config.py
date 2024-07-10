# This file contains the configuration settings for the application.

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    NEWS_API_KEY: str = os.getenv("NEWS_API_KEY")

settings = Settings()
