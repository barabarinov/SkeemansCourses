import requests
from pprint import pprint
from gitignore import TOKEN

api_key = TOKEN
city = 'Kiev'

def get_current_weather(api_key, city):
    return  requests.get(f'http://api.weatherapi.com/v1/current.json?'
                         f'key={api_key}&lang=uk&aqi=yes&alerts=yes&q={city}').json()

def get_forecast_weather(api_key, city):
    return requests.get(f'http://api.weatherapi.com/v1/forecast.json?'
                        f'key={api_key}&q={city}&days=2&aqi=yes&alerts=yes&lang=uk').json()

def get_choice():
    while True:
        try:
            question = int(input("Input '1' to see current weather or '2' to see forecast weather for 2 days: "))
            if question == 1 or question == 2:
                return question
        except ValueError as e:
            print(f'Error{e}')

def main():
        if get_choice() == 1:
            print(f'Current weather in {city} is:')
            pprint(get_current_weather(api_key, city))
        else:
            print(f'Weather forecast for two days in {city} is:')
            pprint(get_forecast_weather(api_key, city))

if __name__ == '__main__':
    main()