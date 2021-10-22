import requests
from pprint import pprint
from secrets import TOKEN

key = TOKEN
language = 'uk'
air_quality = 'yes'
city = 'Kiev'
days = '2'
alerts = 'yes'

parameters_current_weather = {
    'key': key,
    'lang': language,
    'aqi': air_quality,
    'q': city,
    'alerts': alerts
}

parameters_forecast_weather = {
    'key': key,
    'lang': language,
    'aqi': air_quality,
    'q': city,
    'days': days,
    'alerts': alerts
}

response = requests.get(
    'http://api.weatherapi.com/v1/current.json?',
    params=parameters_current_weather
    )
print(f'Current weather in {city} is:\n')
pprint(response.json())

response_two = requests.get(
    'http://api.weatherapi.com/v1/forecast.json?',
    params=parameters_forecast_weather
    )
print(f'\nWeather forecast for two days in {city} is:\n')
pprint(response_two.json())

# f'http://api.weatherapi.com/v1/current.json?key={TOKEN}&lang=uk&aqi=yes&alerts=yes&q={city}').json()

#f'http://api.weatherapi.com/v1/forecast.json?key={TOKEN}&q={city}&days=2&aqi=yes&alerts=yes&lang=uk').json()