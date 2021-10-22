import requests
from pprint import pprint
from secrets import TOKEN

parameters_current_weather = {
    'key': TOKEN,
    'lang': 'uk',
    'aqi': 'yes',
    'q': 'Kiev',
    'alerts': 'yes',
}

parameters_forecast_weather = {
    'key': TOKEN,
    'lang': 'uk',
    'aqi': 'yes',
    'q': 'Kiev',
    'days': '2',
    'alerts': 'yes',
}

response = requests.get(
    'http://api.weatherapi.com/v1/current.json?',
    params=parameters_current_weather)

print(f'Current weather in Kiev is:\n')
pprint(response.json())

response_two = requests.get(
    'http://api.weatherapi.com/v1/forecast.json?',
    params=parameters_forecast_weather)

print(f'\nWeather forecast for two days in Kiev is:\n')
pprint(response_two.json())

# f'http://api.weatherapi.com/v1/current.json?key={TOKEN}&lang=uk&aqi=yes&alerts=yes&q={city}').json()
#f'http://api.weatherapi.com/v1/forecast.json?key={TOKEN}&q={city}&days=2&aqi=yes&alerts=yes&lang=uk').json()