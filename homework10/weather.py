import requests
from pprint import pprint
from gitignore import TOKEN

language = 'lang=uk'
air_quality = 'aqi=yes'
city = 'Kiev'

parameters = {
    TOKEN: TOKEN,
    'language': language,
    'air_quality': air_quality,
    'city': city,
}

def get_current_weather():
    return  requests.get(
        'http://api.weatherapi.com/v1/current.json?',
        params=parameters
        )

def get_forecast_weather():
    return requests.get(
        'http://api.weatherapi.com/v1/forecast.json?',
        params=parameters
        )

def main():
    print(f'Current weather in {city} is:')
    pprint(get_current_weather())

    print(f'Weather forecast for two days in {city} is:')
    pprint(get_forecast_weather())

if __name__ == '__main__':
    main()

# f'http://api.weatherapi.com/v1/current.json?key={TOKEN}&lang=uk&aqi=yes&alerts=yes&q={city}').json()

#f'http://api.weatherapi.com/v1/forecast.json?key={TOKEN}&q={city}&days=2&aqi=yes&alerts=yes&lang=uk').json()