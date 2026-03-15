import redis
from app.config import *

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

def store_memory(session_id, text):

    key = f"session:{session_id}:memory"

    existing = r.get(key)

    if existing:
        r.set(key, existing + "\n" + text)
    else:
        r.set(key, text)

def get_memory(session_id):

    key = f"session:{session_id}:memory"

    return r.get(key) or ""
