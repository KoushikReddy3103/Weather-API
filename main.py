import os
import json
from dotenv import load_dotenv
from cache.redis_client import RedisClient
from weather import Weather_API

load_dotenv()

if __name__ == '__main__':
    city = "Bangalore"
    api_key = os.environ.get("API_KEY")
    api = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/2025-05-19?unitGroup=us&key={api_key}&contentType=json&include=current&elements=datetime,temp,conditions"
    # weather = Weather_API(api)
    
    # Instantiate the Redis Client for Redis connection
    redis_client = RedisClient()
    redis_client.cleanup()

     # Accessing the Cached data
    if not redis_client.redis_client.exists(city):
        # Fetch data from the API or another source
        weather = Weather_API(api)     
        
        current_weather = repr(weather)
        print(json.loads(current_weather))    
        # Set the data in the cache with an expiration time (in seconds)
        redis_client.set(city, current_weather, ttl=43200)
    else:
        weather = redis_client.get(city)

    
    