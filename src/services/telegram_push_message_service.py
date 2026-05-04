import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


logging.basicConfig(level=logging.INFO)

#I'll just hardcode chat_id because I am the only one using this bot for now
def send_telegram_document(Document) -> bool:
    logging.info(f"Sending document {Document} to Telegram with chat_id {CHAT_ID}...")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument" #currently only accepts ZIP or PDF 
    payload = {
        "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
    }
    try:
        response = requests.post(url, data=payload, files={"document": open(Document, "rb")})
        if response.status_code == 200:
            logging.info("Document sent successfully.")
            return True
        else:
            logging.error(f"Failed to send document. Status code: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        logging.error(f"Error sending telegram document: {e}")
        return False
    

print(send_telegram_document("tmp/test.pdf"))