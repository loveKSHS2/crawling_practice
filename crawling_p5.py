#4. CSS Selector를 사용한 크롤링
#CSS 선택 문법을 이용하여 태그 검색
#select 함수 사용
#CSS 선택 문법 참고
#import re
import requests
from bs4 import BeautifulSoup

res = requests.get('http://v.media.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content,'html.parser')

# 태그 검색
soup.find('title')

# select 함수는 리스트 형태로 전체 반환
title = soup.select('title')[0]
print (title)
print (title.get_text())
print()

# 띄어쓰기가 있다면 하위 태그를 검색
title = soup.select('html head title')[0]
print (title.get_text())

title = soup.select('html title')[0]
print (title.get_text())


# > 를 사용하는 경우 바로 아래의 자식만 검색
# 바로 아래 자식이 아니기 때문에 에러 발생
# title = soup.select('html > title')[0]
# print (title.get_text())

# .은 태그의 클래스를 검색
# class가 article_view인 태그 탐색
body = soup.select('.article_view')[0]
print (type(body), len(body))
for p in body.find_all('p'): #해당 클래스에서 p tag로 된것 찾기
    print (p.get_text())
    print()

# div 태그 중 id가 harmonyContainer인 태그 탐색
container = soup.select('#harmonyContainer')
print (container)

# div태그 중 id가 mArticle 인 태그의 하위 태그 중 아이디가 article_title인 태그
title = soup.select('div#mArticle div#harmonyContainer')[0]
print(title)
print(title.get_text())

import re
res = requests.get('http://media.daum.net/economic/')
soup = BeautifulSoup(res.content,'html.parser')

#a태그이면서 href 속성을 갖는 경우 탐색, 리스트 타입으로 links 변수에 저장됨
links = soup.select('a[href]')

for link in links:
    print(link)
    print(link['href'])
    if re.search('http://\w+',link['href']):
        print(link['href'])



res = requests.get('http://land.naver.com/article/divisionInfo.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1168000000&articleOrderCode=&cpId=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&siteOrderCode=&cmplYn=')

soup = BeautifulSoup(res.content, 'html.parser')
link_title = soup.select("#depth4Tab0Content > div > table > tbody > tr > td.align_l.name > div > a")
print(link_title)
##depth4Tab0Content > div > table > tbody > tr > td.align_l.name > div > a.sale_title
link_price = soup.select("#depth4Tab0Content > div > table > tbody > tr > td.num.align_r > div > strong")

for num in range(len(link_price)):
    print(link_title[num].get_text(), link_price[num].get_text())





