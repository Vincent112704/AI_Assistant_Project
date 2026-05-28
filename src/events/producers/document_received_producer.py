from src.events.publisher import publish_message
import logging

logging.basicConfig(level=logging.INFO)

async def document_received_producer(payload: dict):
    logging.info("Publishing document received event: DocumentReceived")
    await publish_message("DocumentReceived", payload)