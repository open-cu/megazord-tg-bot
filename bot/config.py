
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")

BASE_URL = os.getenv("BASE_URL")

SECRET_KEY=os.getenv("SECRET_KEY")

