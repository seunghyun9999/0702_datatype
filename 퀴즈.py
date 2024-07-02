name1=input("이름을 입력하시오")
age1=input('나이를 입력하시오')
email1=input('이메일을 입력하시오')
phone1=input('연락처를 입력하시오')

name2=input("두번째 분 이름을 입력하시오")
age2=input('두번째 분 나이를 입력하시오')
email2=input('두번째 분 이메일을 입력하시오')
phone2=input('두번째 분 연락처를 입력하시오')

입력사항 = {name1:{"나이":age1, "이메일주소": email1, "연락처":phone1},
name2:{"나이":age2, "이메일주소":email2, "연락처":phone2}}
print(name1 , "정보" , 입력사항[name1])
print(name2 , "정보" , 입력사항[name2])




dic = {'달러':1320, '엔':950, '위안':183}
list = [13, 200, 13]
print('철수가 가지고 있는 돈의 원화 가치는 ', list[0]*dic['달러']+list[1]*dic['엔']+list[2]*dic['위안'],'원 입니다.')
