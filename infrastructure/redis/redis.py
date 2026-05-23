# core/redis.py

from redis.asyncio import Redis #basically the same as the normal redis client but with async support so use async/await syntax when interacting with it



redis_client = Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

