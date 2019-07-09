import requests
from bs4 import BeautifulSoup


url = 'https://www.bithumb.com'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')


# #코인이름
# select = soup.select('#tableAsset > tbody > tr > td > p > a > strong')
# coin_name = []
# for list in select:
#  	coin_name.append(list.text)
# print(coin_name)


# # 코인실시간가격
# select = soup.select('#tableAsset > tbody > tr > td > .sort_real')
# coin_price = []
# for list in select:
#     coin_price.append(list.text)
# print(coin_price)


# # 거래금액
# select = soup.select('#tableAsset > tbody > tr > td:nth-of-type(4) > span')
# coin_tprice = []
# for list in select:
#     coin_tprice.append(list.text)
# print(coin_tprice)



# 거래 금액
# total = soup.select('#tableAsset > tbody > tr > td:nth-of-type(4) > span')
# 코인 이름
# name = soup.select('#tableAsset > tbody > tr > td:nth-of-type(1)  > span')
# print(total)
# print(name)


select = soup.select('#tableAsset > tbody > tr')
# print(select)

for list in select:
    total = soup.select('#tableAsset > tbody > tr > td:nth-of-type(4) > span')
    name = soup.select('#tableAsset > tbody > tr > td:nth-of-type(1)  > span')

    with open('bithumb.csv', 'w', encoding= 'utf-8') as f:
        f.write(f'{name}{total}\n')

f.close()


# 결과 : 거래 금액과 코인 이름이 들어간 bithumb.csv 파일 생성