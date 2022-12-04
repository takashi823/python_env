import requests
from bs4 import BeautifulSoup
import datetime
import csv
import os
import shutil
from urllib.parse import urljoin
from time import sleep

url = 'https://python-data-collection.herokuapp.com/mens-fashion'
item_list = []


for i in range(9):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    for elem in soup.find_all("div", class_="col-md-2"):
        item_image_url = urljoin(url, elem.find("img")["src"])
        item_name = elem.find("div", class_="card-body").text.split("\n")[2]
        item_brand = elem.find("div", class_="card-body").text.split("\n")[3]
        item_price = elem.find("div", class_="card-body").text.split("\n")[4].replace(",","")[1:]
        
        item_list.append([item_name ,item_image_url ,item_brand ,item_price])

    if soup.select("a:-soup-contains('Next')"):
        url = urljoin(url,soup.select("a:-soup-contains('Next')")[0]["href"])
        sleep(1)
    else:
        break

# csvファイルの書き込み
csv_header = ["商品名" ,"画像URL" , "ブランド" ,"価格"]
csv_data = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "mens_fashion_" + csv_data + ".csv"

with open(csv_file_name,"w",errors = "ignore") as file:
    writer = csv.writer (file, lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)

# 画像データのダウンロード
path = "/Users/user1/develop/python_env/scrapying/imageFolder"
for item in item_list:
    file_name = item[0] + "." + item[1].split(".")[-1]
    image_path = os.path.join(path ,file_name)
    # 画像のダウンロード
    response = requests.get(item[1],stream=True)
    with open(image_path,"wb") as file:
        shutil.copyfileobj(response.raw,file)