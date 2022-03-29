from gitignore import TOKEN_MAP
from pprint import pprint
import requests

city_name = 'Kyiv,Ua'
city_code = '703448'
bbox = '30,50,31,53,10'
api_key = TOKEN_MAP

def get_weather(api_key, city):
    # url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ua&units=metric&appid={api_key}' #by name of city
    # url = f'http://api.openweathermap.org/data/2.5/box/city?bbox={city}&lang=ua&units=metric&appid={api_key}' #by coordinates for few cities
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city}&lang=ua&units=metric&appid={api_key}' #by city id(city_code)
    return requests.get(url).json()

pprint(get_weather(api_key, city_code))
