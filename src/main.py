from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from src.services import agent_executor_service
import logging
from infrastructure.redis.redis import redis_client
from src.events.producers.message_received_producer import message_received_producer
from src.events.consumers.consume import consume_message_received

logging.basicConfig(level=logging.INFO)
app = FastAPI()



from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

@app.get("/")
async def test_redis():
    return {"redis_status": await redis_client.ping()} 


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
        await message_received_producer(query)
        await consume_message_received()
        # background_tasks.add_task(agent_executor_service.execute_agent, query)
        return JSONResponse(content={"status": "success"}, status_code=200)
    except Exception as e:
        logging.error(f"Error processing Telegram webhook: {e}")
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
    


"""
 I have problems with the pub/sub mechanism of Redis. I might have to look more into how to implement it properly
 
"""
