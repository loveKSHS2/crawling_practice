import requests
from bs4 import BeautifulSoup

res = requests.get('http://media.daum.net/digital/')
soup = BeautifulSoup(res.content, 'html.parser')

# find_all() 메서드를 사용해서 태그와 클래스이름으로 링크가 걸려있는 기사 타이틀을 가져오기
#[------------------------------------------------------]

link_title = soup.find_all('a', {'class' : 'link_txt #article_main'})

for num in range(len(link_title)):
    print(link_title[num].get_text().strip())

