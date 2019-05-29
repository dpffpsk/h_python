import requests
from bs4 import BeautifulSoup


url = 'https://www.bithumb.com'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

#코인이름
#tableAsset > tbody > tr:nth-child(1) > td:nth-child(1) > p > a
# select = soup.select('#tableAsset > tbody > tr > td > p > a > strong')
# coin_name = []
# for list in select:
#  	coin_name.append(list.text)



#코인실시간가격
#tableAsset > tbody > tr > td > .sort_real
# select = soup.select('#tableAsset > tbody > tr > td > .sort_real')
# coin_price = []
# for list in select:
#     coin_price.append(list.text)



#거래금액
#tableAsset > tbody > tr > td > #assetRealBTC
#assetRealBTC2KRW
# select = soup.select('#tableAsset > tbody > tr > td:nth-of-type(4) > span')
# coin_tprice = []
# for list in select:
#     coin_tprice.append(list.text)



select = soup.select('#tableAsset > tbody > tr')
# total = soup.select('#tableAsset > tbody > tr > td:nth-of-type(4) > span')
# name = soup.select('#tableAsset > tbody > tr > td:nth-of-type(1)  > span')
# for list in :
#     total = soup.select(f'{select} > td:nth-of-type(4) > span')
#     name = soup.select(f'{select} > td:nth-of-type(1) > span')
# # #csv파일로 만들기
#     with open('bithumb.csv', 'w', encoding= 'utf-8') as f:
#         f.write(f'{name}{total}\n')
#
# f.close()

