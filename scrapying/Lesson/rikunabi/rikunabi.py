from time import sleep

from bs4 import BeautifulSoup
import requests
import pandas as pd

d_list = []

row = 0
#トップページへのアクセス
base_url = "https://next.rikunabi.com"
top_url = "https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?jb_type_long_cd=0505020000&new_arrvl_only_f=1&prf_cnd_cd=12&prf_cnd_cd=19&prf_cnd_cd=18&curnum={}"

for i in range(3):
    url = top_url.format(1+50*i)

    sleep(3)
    r = requests.get(url, timeout=3)
    r.raise_for_status()

    soup = BeautifulSoup(r.content,'lxml')

    page_urls = soup.select('a:-soup-contains(企業ページ)')

    for page_url in page_urls:
        sleep(3)
        page_r = requests.get(base_url + page_url.get('href'), timeout=3)
        page_r.raise_for_status()

        page_soup = BeautifulSoup(page_r.content, 'lxml')

        company_name = page_soup.select_one('.rnn-breadcrumb li:last-of-type').text
        url_in_tag = page_soup.select_one('.rnn-col-11:last-of-type a')
        company_url = url_in_tag.get('href') if url_in_tag else None

        row +=1
        d_list.append({
            '#':row,
            'company_name':company_name,
            'company_url':company_url
        })
        print(d_list[-1])

df = pd.DataFrame(d_list)
df.to_csv('rikunabi_company_list.csv', index=False, encoding='utf-8-sig')




