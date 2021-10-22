import requests

some_address = requests.get('https://httpbin.org/ip').text
print(some_address)

# pattern = r'\d{2,}\.\d{2,}\.\d{2,}\.\d{2,}.'
# ip = re.search(pattern, some_address).group()
# print(ip)