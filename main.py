import requests
from pprint import pprint

# Uses Open Weather Map

API_Key = '304e06fc96fd015ae8beec97315f12e2'


base_url = "http://api.openweathermap.org/data/2.5/weather?q=Ahoskie&appid=304e06fc96fd015ae8beec97315f12e2"

weather_data = requests.get(base_url).json()

pprint(weather_data)
