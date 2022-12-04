from bs4 import BeautifulSoup


html = """
<body>
    <h1>ページタイトル</h1>
    <h2>演習</h2>
    <p>パラグラフ</p>
    <ol id="step1" class="study-list">
        <li class="python-list">python基礎</li>
        <li class="html-list" value="3">html基礎</li>
        <li class="js-list2" value="10">JavaScript基礎</li>
        <li class="php-list">phpの基礎</li>
    </ol>
</body>
"""

soup = BeautifulSoup(html,'lxml')
print(soup.select('li:-soup-contains("python")'))
