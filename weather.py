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
            self.weather_condition = json.dumps(response.json())
            return        

        else:
            print(f"Error: {response.status_code}. Failed to fetch data.")
            print("Response content:", response.content)
            
    def __repr__(self):
        return self.weather_condition


    def __init__(self, api):
        self.retrieve_weather_data(api)
        