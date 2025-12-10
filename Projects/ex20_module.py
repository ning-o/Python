# 모듈
# 하나의 py파일에 모든 코드와 기능을 작성하여 복잡함. 기능별로 관리하거나 재사용하기 어려움
# 모듈은 여러상수값이나 기능함수들을 가지고 있는 파일의 집합체임 (일종의 폴더)

# 파이썬 모듈의 종류
#1. 표준 모듈: 파이썬을 설치할때 같이 내장되어 설치된 모듈들.. 별도 설치없이 import만하면 사용가능 [표준함수는 import도 없이 사용가능]
#2. 외부 모듈: 사용하려면 별도의 다운로드 및 설치작업이 요구되는 모듈들..[이런 외부모듈을 설치해주는 프로그램 pip(CLI 환경으로 모듈을 설치)]

# 1. 표준 모듈 중 활용이 많은 모듈들
#1). math 모듈 : 수학적인 연산기능(함수)들을 모아놓은 폴더 같은 개념
import math # 모듈 적용

print(math.sin(1))
print(math.cos(1))
print(math.log(100,10)) # x,밑수 .. [뜻: 밑수를 몇승하면 x값이 되는가?]
print(math.floor(3.7))  # 소수점 아래 내리기 >>3
print(math.ceil(3.1))  # 소수점 아래 올리기(반올림이 아님) >>4
# 반올림은 math모듈이 아니라.. 표준함수에 존재함
print(round(3.7)) # >>4
print(round(3.2)) # >>3

#1.1 모듈명이 길면 쓰기 불편해서 다른 이름으로 바꿔 부를 수 있음. as
import math as m
print(m.pow(4,2)) #pow(): 4의 2제곱

#1.2 모듈명없이 필요한 함수만 뽑아서 import
from math import floor,ceil # * << 입력하면 다 가져옴
#뽑아온 함수를 내장함수처럼 그냥 사용할 수 있음
print(floor(2.5))
print(ceil(2.5))

# 함수 말고 값도 ㅗ있음.
print(math.pi)
print()

#2. random 모듈 : 랜덤값 생성, 관련 기능
import random

print(random.random())  # 0.0000 ~ 0.9999999....(0부터 1까지라고 표현함)
# 만약 0~9중의 하나의 숫자를 생성하려면(정수만)
num= math.floor(random.random()*10) # *100이면 0~100
print(num)
# 위 계산을 쉽게해주는 기능함수가 존재함.
print(random.randrange(100))  # range랑 같음 0~99까지
print(random.randrange(5,16)) # 5~15

# 리스트의 요소중 랜덤하게 값을 선택하는 기능
aaa= [1,2,3,4,5]
print(random.choice(aaa))   # aaa리스트 안에서 랜덤
print(random.sample(aaa,3)) # aaa리스트 안에서 요소 3개를 뽑아서 '리스트로 리턴'

# ex) 로또 번호 추천
lotto= list(range(1,46)) #1~45
# 번호 45개중에서 무작위 6개 뽑아오기
nums= random.sample(lotto,6)
print(nums)
# 낮은 번호 순 정렬
nums.sort()
print(nums)
print()
#------------------------------------------
# 3. os 모듈 : 운영체제와 관련된 기능 모듈
import os
print('현재 운영체재:',os.name)     # nt : windows     posix : mac or linux
print('현재 작업폴더:',os.getcwd()) #current wosdrking direcctory
print('현재 폴더안에 있는 파일과 폴더 목록들:',os.listdir())

# 폴더 만들기
# os.mkdir('image')   # 만약 이미 존재하는 폴더라면.. error
if not os.path.isdir('image'):  # 있는지 확인하고 없으면 만들어
    os.mkdir('image')

# 폴더 삭제
# os.rmdir('image')
if os.path.isdir('image'):  # 있는지 확인하고 있으면 지이ㅝ
    os.rmdir('image')

# 파일 이름 변경-- 새로운 파일 만들고 이름 변경하기
with open('nice.txt','w',encoding='utf-8') as file:
    file.write('hello pthon....')

# os.rename('nice.txt', 'good.txt')
if os.path.exists('good.txt'): # 변경하려는 파일명이 있는지 확인
    # 원래는 변경 못하도록 해야하지만 지금은 연습으로 그 파일을 제거하고 이름을 변경
    os.remove('good.txt')
    os.rename('nice.txt','good.txt')

# 명령프롬프트(cmd,터미널)에서 실행했던 명령어를 코드로 실행할 수도 있음.
os.system('dir')    # 맥에서는 명령어가 다름
# os.system('python ex01_ex02_print')

# change directory 명령은 일부 안됨
# os.system('cd ..')

print(os.getcwd())
os.chdir('..')
print(os.getcwd())
print()
#-----------------------------------------

#4). datetime 모듈 : 날짜와 시간 관련 기능 모듈
import datetime

# 현재 날짜와 시간 얻어오기
now= datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 원하는 날짜로 변경 가능
future= now.replace(year=(now.year+1)) # 원본 now는 불변
print(future)
print(now)
print()

# 시간대 용어
# GMT 시간 - 그리니치 천문대 기준 시간.. 경도 0(런던 시간대) . 한국 GMT +9
# UTC 시간 - 1970년 1월 1일 0시0분0초를 기준으로 ms마다 카운트한 원자 시간값. 세계협정시
# UTC의 밀리초(ms) 카운트값이 가장 정확한.. 경과시간을 계산할 수 있어서.. 컴퓨터 공학 같은 곳에서 사용하는 시간

# 그 밀리초의 카운트값을 확인할 수 있음 이를 '타임스탬프'라고 부름
print(now.timestamp())
print()

# 특정 작업의 경과시간을 계산할때 활용
start_time= datetime.datetime.now()
for n in range(10000):
    print(n)

elipsed_time= datetime.datetime.now() - start_time # 타임스탬프의 차이값
print('반복 작업의 경과시간:',elipsed_time)

# datetime 객체는 보유 시간의 차이를 - 연산자로 알아서 잘 계산해줌

# 이 계산 기능을 이용하여.. 날짜 계산 프로그램을 만들 수 있음
a_day= datetime.datetime(2025,11,10)
today= datetime.datetime.now()
print('개강일로부터:',today-a_day)

d_day= datetime.datetime(2026,4,9)
print('수료일:',d_day)
print('수료일까지 남은 날짜:',d_day-today)
print('수료일까지 남은 날짜:',(d_day-today).days,'일')
print()
#------------------------------------------

#5. time 모듈
import time 

print('3초간 프로그램을 잠시 정지했다가.. 다음 코드가 실행되도록..')
time.sleep(3) # 3초간 자다가 알아서 일어나서 다음코드 진행
print('hello python')
print('-'*30)
print()
#-----------------------------------------

#6). urllib 모듈 :  네트워크를 통해 서버의 데이터를 가져오는 모듈
# from urllib import request      # 모듈안에 모듈

# url= request.urlopen('https://n.news.naver.com/article/657/0000045502')
# data= url.read()
# print(data)
# print()
# print(data.decode('utf-8'))