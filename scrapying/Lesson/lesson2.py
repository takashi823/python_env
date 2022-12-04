import re

import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

url = "https://www.python.org/"

r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
post = soup.find('div', class_='blog-widget')

d_list = []
for li in post.find_all('li'):
    post_url = li.find('a').get('href')

    sleep(2)
    post_r = requests.get(post_url)
    post_soup = BeautifulSoup(post_r.content, 'lxml')
    post_h2 = [h2.text for h2 in post_soup.find_all('h2')]
    d= {
        'title':li.find('a').text,
        'url':post_url,
        'date':li.find('time').text,
        'h2':post_h2
    }
    d_list.append()

df = pd.DataFrame(d_list)

df.to_csv('python_web_posts.csv',index=None, encoding='utf-8-sig')
df.to_excel('python_web_posts.xlsx',index=None, encoding='utf-8-sig')

