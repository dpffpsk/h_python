a = list(range(5))
print(a)
# [0, 1, 2, 3, 4]

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4



# sorted : 배열을 정렬해주지만 원본을 바꾸지 않는다.
# sort : 배열을 정렬해주고 원본도 바꾼다.
number=[0,2,1,3]
print(sorted(number))
# [0, 1, 2, 3]

number.sort()
print(number)
# [0, 1, 2, 3]



p={"중국집":123, "일식집":344}
print(p["중국집"])
# 123
print(p["일식집"])
# 344
print(p.values())
# dict_values([123, 344])
print(p.keys())
# dict_keys(['중국집', '일식집'])
