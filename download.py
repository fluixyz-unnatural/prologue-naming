import requests
from bs4 import BeautifulSoup

links = ["http://kitagawa.la.coocan.jp/data/shoji01.html",
 "http://kitagawa.la.coocan.jp/data/shoji02.html",
 "http://kitagawa.la.coocan.jp/data/shoji03.html"]

for index, link in enumerate(links):
    res = requests.get(link)
    soup = BeautifulSoup(res.content,'html.parser',from_encoding='Shift_JIS')
    with open(str(index)+'.html','w') as f:
        f.write(str(soup.html))