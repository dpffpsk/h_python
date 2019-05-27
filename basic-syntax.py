print("얄루")
print("만나서 반갑")
print("'ㅅ'")

a = list(range(5))
print(a)

for i in range(5):
    print(i)

#List
#배열로 여러개의 멤버변수를 가질 수 있으며 index를 통한 접근이 가능, 다른 언어에서는 Array
number=[0,2,1,3]

#sorted함수는 배열을 정렬해주지만 원본을 바꾸지 않는다.
#sort함수는 배열을 정렬해주고 원본도 바꾼다.

print(number.sort())
print(number)

#Dictionary
#Key와 Value로 이루어진 자료구조
#다른 언에서는 map, object라고도 불린다.

p={"중국집":123, "일식집":344}
print(p["중국집"])
print(p["일식집"])
print(p.values())
print(p.keys())