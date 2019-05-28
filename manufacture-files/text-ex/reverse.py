# numbers.txt의 내용을 뒤집어서 저장한다.
with open('numbers.txt', 'r') as f:
    lines = f.readlines()

lines = lines[::-1]
#lines.reverse()

with open('numbers.txt', 'w') as f:
    for line in lines:
        f.write(line)
    f.close()


