import httpx
from dotenv import load_dotenv
import os 
import logging


logging.basicConfig(level=logging.INFO)
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def get_file_service(file_id: str):
    '''
    args: file_id - the file_id of the document sent by the user in Telegrama
    returns: the file path of the document in Telegram's servers
    '''
    logging.info(f"Getting file path for file_id {file_id} from Telegram...")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getFile"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params={"file_id": file_id})
            if response.status_code != 200:
                logging.error(f"Failed to get file path from Telegram for file_id {file_id}. Status code: {response.status_code}, Response: {response.text}")
                return None
            file_path = response.json().get("result", {}).get("file_path", None)
            if file_path is None:
                logging.error(f"No file_path found in Telegram response for file_id {file_id}. Response: {response.text}")
                return None
            logging.info(f"Successfully got file path for file_id {file_id} from Telegram: {file_path}")
            return file_path
        except Exception as e:
            logging.error(f"Error getting file path from Telegram: {e}")
            return None