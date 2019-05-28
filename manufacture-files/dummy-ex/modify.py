# 지원자 > 합격자로
import os

# os.rename('현재파일명', '바꿀 파일명') 파일이름

os.chdir(r'C:\Users\gpljw\PycharmProjects\h_python\manufacture-files\dummy-ex')
filenames = os.listdir('.')

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    # text = os.path.splitext(filename)[0].replace('지원자', '합격자')
    # if txt == '.txt':
    #     os.rename(filename, f'{text}{txt}')

    if txt == '.txt':
        newFilename = filename.replace('지원자', '합격자')
        os.rename(filename, newFilename)

