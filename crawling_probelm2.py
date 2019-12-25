#http://zeroplus1.zc.bz/jh/web/main.php?id=132&category=ETC
#https://toentoi.tistory.com/43

import re
import requests
from bs4 import BeautifulSoup

res = requests.get('http://media.daum.net/economic/')
soup = BeautifulSoup(res.content, 'html.parser')


for href in soup.find_all("a", class_="link_txt #article_main"):
    print(href.get_text())





