from infrastructure.redis.redis import redis_client
import logging

logging.basicConfig(level=logging.INFO)

async def consume_message_received():
    async with redis_client.pubsub() as pubsub:
        await pubsub.subscribe("MessageReceived")
        try:
            while True:
                message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                if message:
                    data = message['data']
                    logging.info(f"Received raw message: {message}")
                    logging.info(f"Received message on channel 'MessageReceived': {data}")
                else:
                    logging.info("No message received, exiting...")
                    break
                    
        except Exception as e:
            logging.error(f"Error consuming messages: {e}")
        finally:
            # Unsubscribe from the channel before closing the socket and retun socket back to the pool
            await pubsub.unsubscribe("MessageReceived") 


"""
Something is wrong here. I have received the message both in the producer and consumer logs but:
    - 
"""