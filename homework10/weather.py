import requests
from secrets import TOKEN
from pprint import pprint, pformat

BASE_API_URL = 'http://api.weatherapi.com/v1'

parameters_forecast_weather = {
    'key': TOKEN,
    'lang': 'uk',
    'aqi': 'yes',
    'q': 'Kiev',
    'days': 2,
    'alerts': 'yes',
}

data = requests.get(
    f'{BASE_API_URL}/forecast.json',
    params=parameters_forecast_weather,
).json()

print(f"Current weather: ")

for key in ['name', 'region', 'country','localtime']:
    print(key.title(), ":", data['location'][key])

for key in ['temp_c', 'feelslike_c']:
    print(key.capitalize(), ':', data['current'][key])

print('Condition: ', data['current']['condition']['text'])