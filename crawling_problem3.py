import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
# div태그 중 id가 mArticle 인 태그의 하위 태그 중 아이디가 article_title인 태그

# div태그 중 id가 mArticle 인 태그의 하위 태그 중 아이디가 article_title인 태그
#title = soup.select('div#mArticle div#harmonyContainer')[0]
#print(title)
#print(title.get_text())

link_title = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li> a > span.ah_k')

for link in link_title:
    print(link.get_text())