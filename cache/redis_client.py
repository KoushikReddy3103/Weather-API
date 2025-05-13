import redis 
import json
import os

class RedisClient:
    def __init__(self):
        # Connect to a local Redis server
        self.redis_client = redis.StrictRedis(
            host=os.getenv('REDIS_HOST', 'localhost'),
            port=int(os.getenv('REDIS_PORT', 6379)),
            db=int(os.getenv('REDIS_DB', 0)),
            decode_responses=True
        )
        # Test the connection
        try:
            self.redis_client.ping()
            pass
        except redis.ConnectionError:
            pass            
        
    def set(self, key, value, ttl=3600):
        self.redis_client.setex(key, ttl, value)

    def get(self, key):
        return self.redis_client.get(key)

    def delete(self, key):
        self.redis_client.delete(key)
    
    def cleanup(self):
        self.redis_client.flushdb()