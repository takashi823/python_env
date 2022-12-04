import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep

top_url = "https://gihyo.jp/"
article_list = []

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 注目記事の取得
for elem in soup.select("ul", class_="m-listitem"):
    
    # 記事の詳細を取得
    article_url = urljoin(top_url,elem.find("a")["href"])
    article_text = ""
    
    for i in range(9):
        response = requests.get(article_url)
        article_soup = BeautifulSoup(response.text, "html.parser")
        
        
    
    
    
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

