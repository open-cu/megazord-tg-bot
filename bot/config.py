import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

API_URL = os.getenv("API_URL")
