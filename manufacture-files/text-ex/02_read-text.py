# readline() : 한 줄씩 읽고 반환
# readlines() : 파일의 모든 줄의 내용 반환(개행문자 까지)

with open('mulcam.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

    # 결과
    # Hapy Hacking 1
    #
    # Hapy Hacking 2
    #
    # Hapy Hacking 3
    #
    # Hapy Hacking 4
    #
    # Hapy Hacking 5



    # all_text = f.read()
    # print(all_text)

    # 결과
    # Hapy Hacking 1
    # Hapy Hacking 2
    # Hapy Hacking 3
    # Hapy Hacking 4
    # Hapy Hacking 5



