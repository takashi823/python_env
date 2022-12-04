from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

from time import sleep


# 1. driverを作成する
service = ChromeService(executable_path='/Users/user1/develop/python_env/scrapying/selenium/tools/chromedriver')

driver = webdriver.Chrome(service=service)

# 2. driver.get()でサイトにアクセスする
driver.get('https://www.google.com')
sleep(3)

# 3. 要素を取得して何らかの処理を行う
search_bar = driver.find_element(By.NAME,'q')
sleep(3)

print("検索")
search_bar.send_keys('python')
sleep(3)

search_bar.submit()
sleep(5)

driver.quit()

