import requests

response_data = requests.get('https://httpbin.org/ip').json()
print(f'Your IP is {response_data["origin"]}')
