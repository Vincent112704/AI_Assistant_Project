from src.events.publisher import publish_message
import logging
from src.utils.preprocess_string import preprocess_string

logging.basicConfig(level=logging.INFO)
async def message_received_producer(query: str):

    logging.info(f"Publishing message received event: MessageReceived with query: {query}")
    query = preprocess_string(query)
    await publish_message("MessageReceived", {"query": query})
    
