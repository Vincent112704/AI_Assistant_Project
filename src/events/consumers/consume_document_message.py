from infrastructure.redis.redis import redis_client
from src.services.get_file_bytes import get_file_bytes
import logging

logging.basicConfig(level=logging.INFO)


async def consume_document_message():
    while True:
        try:
            pubsub = redis_client.pubsub()
            await pubsub.subscribe("DocumentReceived")
            async for message in pubsub.listen():
                if message["type"] == "message":
                    data = message["data"]
                    file_path = data.get("file_path", "")
                    logging.info(f"Received raw message from DocumentReceived channel: {message}")
                    logging.info(f"Consumed DocumentReceived event with data: {data}")
                    file_bytes = await get_file_bytes(file_path)
                    #TODO: 
                    # I would have to create another service to directly use the bytes for my RAG pipeline
                    # Here is the steps:
                    # 1. Use the file bytes to extract the text from the document (using something like PyPDF2 or textract)
                    # 2. Clean and preprocess the extracted text (remove newlines, extra spaces, etc.)
                    # 3. Split the cleaned text into chunks (using something like NLTK or spaCy)
                    # 4. Create embeddings for each chunk (using something like OpenAI's embedding API)
                    # 5. Store the embeddings in a vector database (using chromaDB or prolly pinecone (just for the exposure))
        except Exception as e:
            logging.error(f"Error consuming DocumentReceived event: {e}")