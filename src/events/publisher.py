from infrastructure.redis.redis import redis_client
import json

async def publish_message(channel: str, payload: dict):
    '''
    interface for publishing messages to a Redis channel 
    args:
        channel: the redis channel to publish to
        payload: the message payload to publish (as a dictionary)

    returns: None
    '''
    await redis_client.publish(channel, json.dumps(payload))