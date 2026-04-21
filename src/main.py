from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()


from fastapi import FastAPI

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    '''
    args: Receives user message from telegram
    returns: status 200 if successful
    '''
    try: 
        #todo
        #process the user message in the background
        user_message = await request.json()
        print(user_message)
        return JSONResponse(content={"status": "success"}, status_code=200)
    except Exception as e:
        logging.error(f"Error processing Telegram webhook: {e}")
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
