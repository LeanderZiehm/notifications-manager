from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = FastAPI(title="Telegram Notifier")

class Message(BaseModel):
    text: str

def send_telegram_message(message: str):
    """Send a text message via Telegram Bot API."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception(f"Telegram error: {response.text}")

@app.post("/notify")
async def notify(msg: Message):
    """HTTP endpoint to send a Telegram notification."""
    send_telegram_message(msg.text)
    return {"status": "sent", "text": msg.text}
