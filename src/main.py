from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
import logging

#consumers 
from src.events.consumers.consume_message_received import consume_message_received

#producers
from src.events.producers.message_received_producer import message_received_producer
from src.events.producers.document_received_producer import document_received_producer

#services
from src.services.get_file_service import get_file_service


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
            logging.info("Received a document from Telegram, processing it...")
            file_id = user_message.get('message', {}).get('document', {}).get('file_id', None)

            if file_id is None:
                logging.error("No file_id found in the document message")
                return JSONResponse(content={"status": "error", "message": "No file_id found in the document message"}, status_code=400)
        
            asyncio.create_task(process_document(file_id))
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


async def process_document(file_id: str):
    try:
        file_path = await get_file_service(file_id)

        if file_path is None:
            return
        
        await document_received_producer({file_id: file_id, "file_path": file_path})
        #event should not be sending raw file bytes just the metadata
        #the consumer itself should be responsible for getting the file bytes when it receives the event with the file path. 
        #This is because the producer should only be responsible for publishing the event and not doing any heavy lifting like getting the file bytes which can be done in the consumer when it receives the event. 
        #This also makes the producer more lightweight and faster to publish events.

    except Exception as e:
        logging.error(f"Error processing document with file_id {file_id}: {e}")

"""
Notes:
  - currently working on the telegram webhook for receiving documents, still conflicted on how I want to do it.
  right now, I am considering two options:
    1. when file id is received should I run the process on the background as well at the event emission?
    2. should I just wait for file path to be received but it would block the main thread. This is simpler but I still don't know if it's worth the tradeoff.
 
"""
