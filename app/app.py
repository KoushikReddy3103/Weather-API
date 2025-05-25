from flask import Flask
import requests 
import os
import json
from dotenv import load_dotenv
from cache.redis_client import RedisClient
from weather import Weather_API
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import date

load_dotenv()

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)


@app.route("/<city>", methods=['GET'])
@limiter.limit("10 per day")
def weather_condition(city=None):
    api_key = os.environ.get("API_KEY")
    today = date.today()
    api = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{today}?unitGroup=us&key={api_key}&contentType=json&include=current&elements=datetime,temp,conditions"

    # Instantiate the Redis Client for Redis connection
    redis_client = RedisClient()
    redis_client.cleanup()

    # Accessing the Cached data
    if not redis_client.redis_client.exists(city):
        # Fetch data from the API or another source
        weather = Weather_API(api)     
    
        current_weather = repr(weather)
        # Set the data in the cache with an expiration time (in seconds)
        redis_client.set(city, current_weather, ttl=43200)
    else:
        weather = redis_client.get(city)
    
    return json.loads(current_weather)


if __name__ == '__main__':
    app.run(debug=True)