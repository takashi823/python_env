import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=4kNt62PptEQ"
response = requests.get(url)

with open(response.text, encoding="utf-8") as file:
  soup = BeautifulSoup(file, "html.parser")
  print(soup.find("h1"))
  