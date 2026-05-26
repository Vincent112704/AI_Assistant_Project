from infrastructure.redis.redis import redis_client
import logging

logging.basicConfig(level=logging.INFO)

async def consume_message_received():
    while True:
        try:
            pubsub = redis_client.pubsub()
            await pubsub.subscribe("MessageReceived")
            async for message in pubsub.listen():
                if message["type"] == "message":
                    data = message["data"]
                    logging.info(f"Received raw message from MessageReceived channel: {message}")
                    logging.info(f"Consumed MessageReceived event with data: {data}")

        except Exception as e:
            logging.error(f"Error consuming MessageReceived event: {e}")



'''
Something is wrong here. I have received the message both in the producer and consumer logs but:
    1. fastapi-debug-container  | INFO:     Waiting for background tasks to complete. (CTRL+C to force quit)
      - Something is blocking the program from exiting after processing the message.
      - hence, it never reaches the finally block to unsubscribe and close the pubsub connection, which might be causing some issues with the Redis connection pool.
    2. I might have to explore cleaner ways to do the clean up after using sockets


Notes:
 - Producer is working fine, it is publishing the message to the channel as well as the payload
 - Consumer is able to subscribe based on the logs but it is not exiting
 - 
'''