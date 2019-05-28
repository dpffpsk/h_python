import os
# os.chdir('폴더이름') 지정한 폴더로 이동
# os.list('폴더경로') 폴더에 저장된 전체 파일목록을 list로 반환
# os.rename('현재파일명', '바꿀 파일명') 파일이름
# os.path.splitext('파일이름') 파일 경로와 확장자를 분리하여 반환

# 폴더경로 C:\Users\gpljw\PycharmProjects\h_python\manufacture-files\dummy-ex
# filename = os.path.splitext(r'C:\Users\gpljw\PycharmProjects\h_python\manufacture-files\dummy-ex\dummy.py')
# print(filename)

os.chdir(r'C:\Users\gpljw\PycharmProjects\h_python\manufacture-files\dummy-ex')
filenames = os.listdir('.')

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    if txt == '.txt':
        os.rename(filename, f'지원자_{filename}')