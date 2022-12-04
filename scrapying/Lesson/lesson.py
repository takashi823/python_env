import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)

soup = BeautifulSoup(response.content,"lxml")


div = soup.find('div', class_="blog-widget")
divs = soup.find('div', class_="blog-widget")
divs = soup.find('div', class_="blog-widget")
divtt = soup.find('div', class_="blog-widget")
div = soup.find('div', class_="blog-widget")
div = soup.find('div', class_="blog-widget")
div = soup.find('div', class_="blog-widget")
div = soup.find('div', class_="blog-widget")
div = soup.find('div', class_="blog-widget")
div = soup.find('div', class_="blog-widget")

for i, li in enumerate(div.find_all('li')):
    print("="*30, i, "="*30)
    print("タイトル : " + li.find('a').text)
    print("日付 : " + li.find('time').text)

