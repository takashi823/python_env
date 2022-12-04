import requests
from bs4 import BeautifulSoup
import datetime
import csv
from time import sleep

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
items = soup.select("ol.row li")
item_list = []

# データの抽出
for item in items:
    item_name = item.select("h3 a")[0].text
    item_url = item.select("h3 a")[0]["href"]
    item_price = item.select("p.price_color")[0].text
    item_stock = item.select("p.instock.availability")[0].text.strip()

    # 詳細ページから商品コードを取得
    detail_url = url + item_url
    response = requests.get(detail_url)
    soup = BeautifulSoup(response.text, "html.parser")
    item_code = soup.select("table td")[0].text.strip()

    # リストに抽出したデータを追加
    item_list.append([item_name,item_url, item_price, item_stock, item_code])
    sleep(1)

# csvファイルの作成
csv_header = ["商品名" ,"URL" , "価格" ,"在庫", "商品コード"]
csv_data = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "item_data_" + csv_data + ".csv"

with open(csv_file_name,"w",errors = "ignore") as file:
    writer = csv.writer (file, lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)
