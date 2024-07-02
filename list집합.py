seunghyun = ["전승현", "26", "010-0000-0000"]

print(type(seunghyun))

print(seunghyun[0])

name = seunghyun[0]
age = seunghyun[1]
phone = seunghyun[2]

print('이름은 ' + name + ' 나이는 ' + age + ' 전화번호는 '+phone)

집합 = [['가', '나', '다'], ['라', '마', '바'],['사','아']]
print(집합[0][1])
# 연달아서 쓰면 안에 있는게 나옴

# 중간에 안전과 관련된 계산기 만드는 과제 있음
# 예를 들면 붕괴나 인장강도 피로도 내연성 같은거면 좋을지도 팀별로 함

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]

print(result)

print(len(numbers))

# 리스트에 요소 추가하기
last = [1,2,3,4]
last.append(30)
# 변수를 추가는 것임 한마디로 위에 함수last는 1,2,3,4,30 인거임
print(last)
last.remove(1)
# 변수를 지우는 것임 한마디로 위에 함수는 2,3,4,30
print(last)


