import requests

url = "https://gihyo.jp/"
response = requests.get(url)
print(response.status_code)
print(response.headers)
print(response.content)
