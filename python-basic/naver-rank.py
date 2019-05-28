# naver에서 html파일을 가지고온다.
# BeautifulSoup를 이용해서 parsing 한다.
# 실시간 검색어 10위까지 출력한다.
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

# #검색어
# select = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
# #검색순위
# number = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_r')
#
# for list in select:
# 	print(list.text)

#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(15) > a
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_r