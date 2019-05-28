import random

# menu 리스트를 만들어주세요.
menu=["쌀국수","떡볶이","감자탕","수제비","칼국수","쫄면","삼겹살","뼈해장국"]
phonebook={"쌀국수":123,"떡볶이":443, "감자탕":897, "수제비":394, "칼국수":920, "쫄면":748,"삼겹살":196,"뼈해장국":450}

choice = random.choice(menu)
print(f'오늘의 메뉴는 {choice} 입니다.')
print(f'전화번호 {phonebook[choice]}')