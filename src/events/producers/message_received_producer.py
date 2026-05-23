from src.events.publisher import publish_message
import logging

logging.basicConfig(level=logging.INFO)
async def message_received_producer(query: str):

    logging.info(f"Publishing message received event: MessageReceived with query: {query}")
    await publish_message("MessageReceived", {"query": query})
    
