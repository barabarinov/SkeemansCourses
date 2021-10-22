import requests

response = requests.get('https://httpbin.org/ip').json()
print(f'Your IP is {response}')

# pattern = r'\d{2,}\.\d{2,}\.\d{2,}\.\d{2,}.'
# ip = re.search(pattern, some_address).group()
# print(ip)