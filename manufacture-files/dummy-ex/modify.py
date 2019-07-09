import os

os.chdir(r'C:\Users\gpljw\PycharmProjects\python-basic\manufacture-files\dummy-ex')
filenames = os.listdir('.')

for filename in filenames:
    txt = os.path.splitext(filename)[-1]

    if txt == '.txt':
        newFilename = filename.replace('지원자', '합격자')

        # os.rename('현재파일명', '바꿀 파일명') 파일이름
        os.rename(filename, newFilename)


# 결과 : '지원자' -> '합격자'
# $ python modify.py
# 합격자_1_이길동.txt
# 합격자_2_조소미.txt
# 합격자_3_한수진.txt