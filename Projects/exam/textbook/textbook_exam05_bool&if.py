# #----------------------[직접 해보는 손코딩]--------------------------

# # not 연산자 조합하기 --p.159
# x= 10
# under_20= x<20
# print('under_20:',under_20)
# print('not under_20:',not under_20)

# # 조건문의 기본 사용 --p.164
# number = int(input('정수 입력: '))

# if number > 0 : # 양수 조건
#     print('양수입니다.')

# if number < 0 : # 음수 조건
#     print('음수입니다.') 

# if number == 0 : # 0 조건
#     print('0입니다.')
# print()

# # 끝자리로 짝수와 홀수 구분 --p.169
# number = input('홀짝 구분 정수 입력: ')
# last_character= number[-1] # 마지막 자리 숫자를 추출
# last_number= int(last_character) # 추출 후 숫자로 변환

# if last_number == 0 \
#     or last_number ==2 \
#     or last_number ==4 \
#     or last_number ==6 \
#     or last_number ==8 :
#     print('짝수입니다.')

# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9 :
#     print('홀수입니다.')

# # in 문자열 연산자를 활용해서 홀짝 구분 --p.170
# in_number= input('in정수입력: ')
# in_last_character=number[-1]

# if in_last_character in '02468' :
#     print('짝수입니다.')

# if in_last_character in '13579' :
#     print('홀수입니다.')

# # 나머지 연산자를 활용해서 짝수와 홀수 구분 --p.171
# numberr= int(input('%정수 입력: '))

# if numberr % 2 == 0 :
#     print('짝수입니다.')

# if numberr % 2 == 1 :
#     print('홀수입니다.')

# if조건문에 else 구문을 추가해서 홀짝 구분하기 -- p.177
# number = input('정수 입력: ')
# number = int(number)

# if number % 2 == 0 :
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')
# print()

# # 유머를 조건문으로 구현하기 --p.181
# score= float(input('학점 입력: '))

# if score == 4.5 :
#     print("당신의 학점은 '신'급 입니다.")
# elif 4.2 <= score :
#     print("당신의 학점은 '교수님의 사랑'급 입니다.") 
# elif 3.5 <= score :
#     print("당신의 학점은 '현 체제의 수호자'급 입니다.")
# elif 2.8 <= score :
#     print("당신의 학점은 '일반인'급 입니다.")
# elif 2.3 <= score :
#     print("당신의 학점은 '일탈을 꿈꾸는 소시만'급 입니다.")
# elif 1.75 <= score :
#     print("당신의 학점은 '오락문화의 선구자'급 입니다.")
# elif 1.0 <= score :
#     print("당신의 학점은 '불가촉천민'급 입니다.")
# elif 0.5 <= score :
#     print("당신의 학점은 '자벌레'급 입니다.")
# else:
#     print("당신의 학점은 '주그세요 그냥'급 입니다.")
# print()

# # False로 변환되는 값
# print('# if조건문에 0 넣기')
# if 0:
#     print("0은 True로 변환됩니다")
# else:
#     print('0은 False로 변환됩니다.')
#     print()

# print('# if 조건문에 빈 문자열 넣기')
# if "":
#     print('빈 문자열은 True로 변환됩니다.')
# else:
#     print('빈 문자열은 False로 변환됩니다.')

# 태어난 연도를 입력받아 띠를 출력하는 프로그램
# str_input=input('태어난 연도 입력: ')
# birth_year= int(str_input)%12
# if birth_year==0:
#     print('원숭이 띠입니다.')
# elif birth_year==1:
#     print('닭 띠입니다.')
# elif birth_year==2:
#     print('개 띠입니다.')
# elif birth_year==3:
#     print('돼지 띠입니다.')
# elif birth_year==4:
#     print('쥐 띠입니다.')
# elif birth_year==5:
#     print('소 띠입니다.')
# elif birth_year==6:
#     print('범 띠입니다.')
# elif birth_year==7:
#     print('토끼 띠입니다.')
# elif birth_year==8:
#     print('용 띠입니다.')
# elif birth_year==9:
#     print('뱀 띠입니다.')
# elif birth_year==10:
#     print('말 띠입니다.')
# elif birth_year==11:
#     print('양 띠입니다.')

# 간단한 대화 프로그램

import datetime

now= datetime.datetime.now()


hello=input("채팅 입력: ")

if '안녕' in hello or 'Hi' in hello or 'ㅎㅇ' in hello :
    print('안녕하세요!')
elif '몇시' in hello or '몇 시' in hello or 'What Time' in hello :
    print(f'지금은 {now.hour}시 {now.minute}분 입니다.')
else:
    print(hello)

