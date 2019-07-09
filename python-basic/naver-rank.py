# naver에서 html파일을 가지고온다.
# BeautifulSoup를 이용해서 parsing 한다.
# 실시간 검색어 출력한다.

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

index=0
result = soup.find_all('span', class_='ah_k')
for results in result:
  index = index+1
  print(index, results.text)
