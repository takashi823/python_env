import csv
import datetime

csv_header = ["ランキング","商品名","評価","価格"]

#サンプルデータ
ranking_data = [
    ["1", "商品1", "5", "1,200"],
    ["2", "商品2", "5", "1,300"],
    ["3", "商品3", "4.5", "10,200"],
    ["4", "商品4", "4.2", "1,000"],
    ["5", "商品5", "3.8", "1,000"]
]


csv_data = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "ranking_data_" + csv_data + ".csv"

with open(csv_file_name,"w", errors = "ignore") as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(ranking_data)

