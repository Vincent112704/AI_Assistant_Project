import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)


def send_telegram_message(chat_id: str, message: str) -> bool:
    # if sending document
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument" #currently only accepts ZIP or PDF 
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logging.info("Message sent successfully.")
            return True
        else:
            logging.error(f"Failed to send message. Status code: {response.status_code}")
            return False
    except Exception as e:
        logging.error(f"Error sending telegram message: {e}")
        return False
    
    #not final yet too lazy to continue

    # else if 
    # do something if sending just a message w/o document

    # else:
    # do something if neither of the above