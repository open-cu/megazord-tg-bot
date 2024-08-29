import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

SERVICE_EMAIL = os.getenv("SERVICE_EMAIL")
SERVICE_PASSWORD = os.getenv("SERVICE_PASSWORD")

API_URL = os.getenv("API_URL")
