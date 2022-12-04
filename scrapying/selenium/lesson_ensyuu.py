from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from time import sleep


# driverを作成する
options = ChromeOptions()
options.add_argument('--incognito')
service = ChromeService(executable_path='/Users/user1/develop/python_env/scrapying/selenium/tools/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

# サイトにアクセスする
driver.get('https://news.yahoo.co.jp/')
sleep(3)

# 処理
# 検索ボックスの取得
search_box = driver.find_element(By.CSS_SELECTOR,'input.sc-kgoBCf')
sleep(2)

# 検索ワードの入力
search_box.send_keys("機会学習")
sleep(2)

# 検索ボタンの押下
search_box.submit()

# [もっと見る]ボタンの押下
while True:
    # スクロールする
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)

    # ボタンのCSSセレクターを取得する
    button = driver.find_elements(By.CSS_SELECTOR, 'div.newsFeed > div > span > button')
    sleep(2)

    # ボタンを押下する
    if button:
        button[0].click()
    else:
        break

a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.newsFeed_item_link')

for i,a_tag in enumerate(a_tags):
    print('=' * 30, i, '=' * 30)
    print(a_tag.find_element(By.CSS_SELECTOR,'.newsFeed_item_title').text)
    print(a_tag.get_attribute('href'))



# newsリストの取得
#news_list = driver.find_elements(By.CSS_SELECTOR,'div.sc-iTuVof li')
#for news in news_list:
#     print(news.find_element(By.CSS_SELECTOR,'div.newsFeed_item_title').text)


sleep(5)
driver.close()
