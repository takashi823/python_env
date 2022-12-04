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

a_tag = driver.find_element(By.CSS_SELECTOR, 'div.sc-iqtXtF li:nth-of-type(3) > a')
sleep(3)

a_tag.click()
sleep(5)

driver.close()

