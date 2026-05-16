from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from src.services import agent_executor_service
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

logging.info(type(agent_executor_service.execute_agent))
logging.info(callable(agent_executor_service.execute_agent))

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request, background_tasks: BackgroundTasks):
    '''
    args: Receives user message from telegram
    returns: status 200 if successful
    '''
    try: 
        #todo
        #process the user message in the background
        user_message = await request.json()
        query = user_message.get("message", {}).get("text", "")
        background_tasks.add_task(agent_executor_service.execute_agent, query)
        return JSONResponse(content={"status": "success"}, status_code=200)
    except Exception as e:
        logging.error(f"Error processing Telegram webhook: {e}")
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
