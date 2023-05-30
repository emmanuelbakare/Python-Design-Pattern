#complex subsystem
import requests 
import json 
import datetime


class WeatherAPI:
    def __init__(self,api_key):
        self.api_key = api_key

    def get_current_weather(self, city):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}' 

        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            temperature = round(data['main']['temp'] - 273.15,1)
            description = data['weather'][0]['description']
            return f'Current weather in {city}: {temperature}, {description}'
        else:
            return 'Unable to retrieve weather information'

    def get_forecast(self,city):
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}' 
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            forecast = []
            for item in data['list']:
                timestamp = item['dt']
                date = datetime.datetime.fromtimestamp(timestamp)
                temperature = round(item['main']['temp'] - 273.15,1)
                description = item['weather'][0]['description']
                forecast.append({'date':date, 'temperature':temperature, 'description':description})
            return forecast
        else:
            return 'Unable to retrieve weather information'


    def get_location(self,ip_address):
        url = f'http://ip-api.com/json/{ip_address}'
        response = requests.get(url) 
        if response.status_code == 200:
            data = json.loads(response.text)
            city = data['city']
            country = data['country']
            return {'city':city, 'country':country}
        else:
            return 'Unable to retrieve location information'


