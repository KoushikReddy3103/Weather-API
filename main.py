import requests
import json

class Weather_API:
    def retrieve_weather_data(self, api):
        try:
            response = requests.get(api)
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        
        if response.status_code == 200:
            print("Successfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(f"Error: {response.status_code}. Failed to fetch data.")
            print("Response content:", response.content)
    
    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    
    def __init__(self, api):
        self.retrieve_weather_data(api)

if __name__ == '__main__':
    city = "Bangalore"
    api = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key=LLLHMXFW2KK7XQ6N2ZHM3F22T&contentType=json"
    weather_api = Weather_API(api)
