from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

from time import sleep


# driverを作成する
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
#options.add_argument('--headless')

service = ChromeService(executable_path='/Users/user1/develop/python_env/scrapying/selenium/tools/chromedriver')
driver = webdriver.Chrome(service=service,options=options)

# driver.get()でサイトにアクセスする
driver.get('https://news.yahoo.co.jp')
sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, 'input.sc-kgoBCf')
sleep(3)

search_box.send_keys("python")
sleep(3)

# search_box.clear()
text = search_box.get_attribute('value')
search_box.send_keys(Keys.BACKSPACE * len(text))
sleep(3)

search_box.send_keys("機械学習")
sleep(3)

search_box.submit()
sleep(3)

driver.close()

