# 파일을 여는 함수 open
# 1번째 매개변수는 파일 이름이 옴
# 2번째 매개변수로 open option
# r : 읽기
# w : 쓰기 - write(overwrite)
# a : 추가 - append

'''
파이썬에서 with 구문은 '컨텍스트 매니저'이다.
with 블럭을 통해 명시적으로 파일을 불러서 작업하는
코드 블럭을 만들 수 있다.
with 블럭이 종료되면 자동으로 파일을 닫는다.
'''

f = open('mulcam.txt', 'w')
for i in range(1,6):
    f.write(f'Hapy Hacking {i}\n')
f.close()

# 결과
# Hapy Hacking 1
# Hapy Hacking 2
# Hapy Hacking 3
# Hapy Hacking 4
# Hapy Hacking 5
