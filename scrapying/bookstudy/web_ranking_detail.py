import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep

url = "https://python-data-collection.herokuapp.com/ranking"
item_list = []

for i in range(9):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #商品ごとの情報を取得
    for elem in soup.find_all("div", class_="col border"):
        item_ranking = int(elem.find("span", class_="badge bg-secondary").text.replace("#",""))
        # 相対URLを絶対URLに変換
        item_url = urljoin(url,elem.a["href"])
        response = requests.get(item_url)
        soup_detail = BeautifulSoup(response.text, "html.parser")

        # 商品情報
        item_name =soup_detail.find("p",class_="card-text").text
        item_os = soup_detail.select("ul.list-group.list-group-flush > li:nth-of-type(1)")[0].text.split("/")[0].strip()
        item_maker = soup_detail.select("ul.list-group.list-group-flush > li:nth-of-type(1)")[0].text.split("/")[1].strip()
        item_size = soup_detail.select("ul.list-group.list-group.list-group-flush > li:nth-of-type(2)")[0].text.split("/")[0].strip().replace("型(インチ)","")
        item_weight = soup_detail.select("ul.list-group.list-group.list-group-flush > li:nth-of-type(2)")[0].text.split("/")[1].strip().replace("kg","")

        # class属性の評価を抽出

        item_rating = float(soup_detail.select("ul.list-group.list-group.list-group-flush > li:nth-of-type(3)")[0].text.split("/")[0])
        item_no_of_rating = float(soup_detail.select("ul.list-group.list-group.list-group-flush > li:nth-of-type(3)")[0].text.split("/")[1].replace(",","").replace("個の評価",""))
        item_price = int(soup_detail.select("ul.list-group.list-group.list-group-flush > li:nth-of-type(4)")[0].text.replace(",","")[1:])

        # データをリストに追加
        item_list.append([item_ranking, item_name, item_url, item_os,item_maker,item_size,item_weight, item_rating, item_no_of_rating, item_price])
        sleep(1)

    # 次のページにいけなければ終了:aタグ配下に"Next"の文字を含むものを抽出できれば。
    if soup.select("a:-soup-contains('Next')"):
        # 次のページの相対パスを絶対パスに変換
        url = urljoin(url,soup.select("a:-soup-contains('Next')")[0]["href"])
        # 一定時間をあける。１秒。
        sleep(1)
    else:
        break

# 抽出データのcsvファイル出力
csv_header = ["ランキング","商品名" ,"URL" ,"OS" ,"メーカー" ,"サイズ（インチ）" ,"重量(kg)" ,"評価" ,"評価数" ,"価格" ]
csv_date = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "notebook_detail" + csv_date + ".csv"
with open(csv_file_name,"w", errors="ignore") as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)

