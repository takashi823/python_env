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
        item_name =elem.find("h5").text
        # 相対URLを絶対URLに変換
        item_url = urljoin(url,elem.a["href"])
        # class属性の評価を抽出
        item_rating = float(elem.find("p",class_="card-text")["class"][1].replace("star-rating-",""))
        item_no_of_ratings = int(elem.find("p", class_="card-text").span.text.replace(",",""))
        item_price = int(elem.find("span", class_="text-danger").text.replace(",","")[1:])
        # データをリストに追加
        item_list.append([item_ranking, item_name, item_url, item_rating, item_no_of_ratings, item_price])
        
        # 次のページにいけなければ終了:aタグ配下に"Next"の文字を含むものを抽出できれば。
        if soup.select("a:-soup-contains('Next')"):
            # 次のページの相対パスを絶対パスに変換
            url = urljoin(url,soup.select("a:-soup-contains('Next')")[0]["href"])
            # 一定時間をあける。１秒。
            sleep(1)
        else:
            break
# 抽出データのcsvファイル出力
csv_header = ["ランキング","商品名" ,"URL" ,"評価" ,"評価数" ,"価格" ]
csv_date = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "notebook_" + csv_date + ".csv"
with open(csv_file_name,"w", errors="ignore") as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)











