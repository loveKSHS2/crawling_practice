#2.4. BeautifulSoup 라이브러리 활용 string 검색 예제
#태그가 아닌 문자열 자체로 검색
#문자열, 정규표현식 등등으로 검색 가능
#문자열 검색의 경우 한 태그내의 문자열과 exact matching인 것만 추출
#이것이 의도한 경우가 아니라면 정규표현식 사용

import requests
from bs4 import BeautifulSoup
import re

res = requests.get('http://v.media.daum.net/v/20170518153405933')
soup = BeautifulSoup(res.content, 'html5lib')

print (soup.find_all(string='오대석'))
print (soup.find_all(string=['[이주의해시태그-#네이버-클로바]쑥쑥 크는 네이버 AI', '오대석']))
#string 여러개 찾기 기능

print (soup.find_all(string='AI'))
print (soup.find_all(string=re.compile('AI'))[0])
#문자열 검색의 경우 한 태그내의 문자열과 exact matching인 것만 추출
print (soup.find_all(string=re.compile('AI')))



