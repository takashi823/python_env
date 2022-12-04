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

height = driver.execute_script('return document.body.scrollHeight')
# while height < 3000:
driver.execute_script(f'window.scrollTo(0,{height})')
    # height += 100
sleep(3)


driver.close()

