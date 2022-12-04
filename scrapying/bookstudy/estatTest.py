import requests
import csv
import datetime


APP_ID = "4c31e0876e294e02b16c401d44344bd064f476ae"

url = "http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData"
# 品目分類
stats_data_id = "0003343671"
code_category_01 = "010120000"
params = {"appId":APP_ID, "statsDataId":stats_data_id, "cdCat01":code_category_01,
"sectinHeaderFlg":2,"explanationGetFlg":"N","metaGetFlg":"N","annotationGetFlg":"N"}

response = requests.get(url, params=params, stream=True)

csv_date = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "estat_bread_comsumption_" + csv_date + ".csv"
with open(csv_file_name, 'w') as file:
    file.write(response.text)
