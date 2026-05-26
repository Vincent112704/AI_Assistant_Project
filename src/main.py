from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
import logging
from src.events.consumers.consume import consume_message_received
# from infrastructure.redis.redis import redis_client
from src.events.producers.message_received_producer import message_received_producer
import asyncio

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app):
    # Initialize resources here (e.g., database connections, Redis clients)
    # await redis_client.initialize()  # Example: Initialize Redis client
    asyncio.create_task(consume_message_received())
    logging.info("Application startup: Resources initialized")
    
    yield  # This is where the application runs
    
    # Clean up resources here (e.g., close database connections, Redis clients)
    # await redis_client.close()  # Example: Close Redis client
    logging.info("Application shutdown: Resources cleaned up")


app = FastAPI(lifespan=lifespan)



# @app.get("/")
# async def test_redis():
#     return {"redis_status": await redis_client.ping()} 


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
        # logging.info(f"Received message from Telegram: {user_message}") uncomment if you want to see the JSON message from Telegram
        hasDocument = user_message.get("message", {}).get("document", None) is not None
        
        if hasDocument:
            logging.info("Received a document, ignoring for now")
            return JSONResponse(content={"status": "received document, processing it asynchronously"}, status_code=202)
        else: 
            query = user_message.get("message", {}).get("text", "")
            asyncio.create_task(message_received_handler(query))
            
            # background_tasks.add_task(agent_executor_service.execute_agent, query)
            return JSONResponse(content={"status": "processing it asynchronously"}, status_code=202)
    except Exception as e:
        logging.error(f"Error processing Telegram webhook: {e}")
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
    
async def message_received_handler(query: str):
    try:
        await message_received_producer(query)
    except Exception as e:
        logging.error(f"Error in message_received_handler: {e}")

"""
Notes:
  - might have to add something like asyncio.create_task() to run the producer/consumer in the background without blocking 
  the main thread. Telegram has to receive a response within a certain time frame otherwise it will consider the webhook request failed, 
  so we can't have any long running tasks in the main thread.
  - 
 
"""
