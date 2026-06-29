from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ALLOWED_USERS = (
    int(user_id.strip())
    for user_id in os.getenv("ALLOWED_USERS", "").split(",")
    if user_id.strip()
)
