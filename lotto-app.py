# 1~45의 숫자 중에서 중복되지 않는 랜덤 6개 숫자를 뽑아서 출력하는 앱을 만들어 보세용
import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
lotto.sort()
print(f"행운의 숫자는 {lotto} 입니다.")