import httpx
import os
import logging
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(level=logging.INFO)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

FILE_PATH = 'documents/file_0.pdf'

async def get_file_bytes(file_path: str) -> bytes:
    '''
    args: file_path - the file path of the document in Telegram's servers
    returns: the actual file bytes of the document
    '''

    url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file_path}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.content #this is the raw bytes

        except Exception as e:
            logging.error(f"Error getting file bytes from Telegram: {e}")
            return None