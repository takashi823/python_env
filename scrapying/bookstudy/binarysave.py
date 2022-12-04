import requests
from bs4 import BeautifulSoup
import os
import shutil

# urlの指定
url = "https://python-data-collection.herokuapp.com/save-data"
response = requests.get(url)

#データの抽出方法を指定
soup = BeautifulSoup(response.text, "html.parser")
pdf_url = soup.find("a", class_="pdf")["href"]

# データの保存場所とファイル名指定
path = r"/Users/user1/develop/python_env/scrapying"
filename = pdf_url.split("/")[-1]
file_path = os.path.join(path, filename)

# データの保存
response = requests.get(pdf_url, stream=True)
with open(file_path,"wb") as file:
    shutil.copyfileobj(response.raw,file)
    