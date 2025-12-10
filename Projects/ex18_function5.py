# 파이썬의 표준(내장)함수 중 활용이 많은 15개정도 소개

#1. print() : 데이터를 화면에 출력
#2. input() : 키보드로부터 문자열로 데이터를 입력받아서 리턴
#3. type()  : 데이터 또는 변수의 타입을 리턴
#4. len()   : 문자열이나 리스트등의 길이를 알려주는 기능함수
message= 'Hello python'
print(len(message))

aaa=[10,20,30]
print(len(aaa))
aaa.append(40)
print(len(aaa))
print()
#5. sum()   : 반복 가능한 데이터의 모든 요소 합을 리턴
total= sum(aaa)
print(total)

#6. min(), max() : 최소값, 최대값 리턴
bbb= [10,72,54,3,180,42,1500]
print(max(bbb))
print(min(bbb))

#7. abs()   : 절대값 함수
num= 100
print(abs(num))
num= -100
print(abs(num))
print()

#8. range() : 지정된 범위의 숫자 시퀀스를 만들어 줌
aa= range(5) #0~4
print(aa)
for n in aa:
    print(n)

#9. list()  : 다른 형태의 iterable(반복할 수 있는) 객체들을 모두 list 타입으로 변환하거나, 빈 리스트 생성도 가능
aa= []
print(aa)

bb= list()
print(bb)

cc= list('Hello')
print(cc) # ['H','e','l','l','o']

dd= list((10,20,30))
print(dd) # 튜플도 리스트로 변환

ff= list({'name':'sam','age':20})
print(ff) # key값들 만으로 리스트를 생성

gg= list({'지희','지희',30}) #set타입(중복 저장 안되는 타입)
print(gg)

print(range(5))
print(list(range(5)))

aa= [n for n in range(5)] # 위랑 같은 기능
print(aa)

# [번외] 문자열의 연산자 +, * ---> 리스트에도 가능
ee= [10,20,30] + [4,5,6]
print(ee)

ee= [10]*5 # 요소값 10을 5개..
print(ee)

ee= [1]*20 + [0]*7
print(ee)
print(len(ee))
print()

#10. map()  : 반복 가능한 객체의 각 요소에 특정 함수를 적용한 결과 리스트를 리턴
aaa= [10,20,30]
bbb= map(lambda n:n*2, aaa) # map()은 연산식
print(bbb)
print(list(bbb))

#11. filter()   : 반복 가능한 객체의 각 요소에 특정 함수의 조건값이 True인 결과요소만 뽑아서 리스트를 리턴
aaa= [10,50,47,85,60]
bbb= filter( lambda n:n>50, aaa) # filter()는 조건식
print(list(bbb))

#12. sorted()   : 반복 가능한 객체(리스트 등)의 정렬된 새로운 리스트를 반환
aaa=[40,23,78,5,64,1500,72]
bbb= sorted(aaa) # 오름차순
print(bbb)

ccc= sorted(aaa, reverse=True) # 내림차순
print(ccc)

#13. enumerate()    : 순서가 있는 자료형(리스트,튜플)에 인덱스 값을 포함하는 (index,value)튜플로 리턴해주는 기능
aaa=['sam','robin','hong']
for v in aaa:
    print(v)
print()

for t in enumerate(aaa):
    print(t[0],t[1]) # (index,value)
print()

for idx,value in enumerate(aaa):
    print(idx,value)
print()

#14. zip()  : 여러개의 리스트의 요소들을 병렬로 묶어서 튜플의 반복자를 만들어냄.
name_list= ['sam','robin','hong','park']
age_list= [20,23,28,15]
people= zip(name_list, age_list)
print(list(people))

# 튜플데이터를 dictionary 타입으로 바꿀 수 있음.s
people= zip(name_list, age_list)
vvv= dict(people)
print(vvv)

#15. any(), all()
# any : 요소중에 하나라도 조건에 맞으면 True ,요소들 중에 하나라도 조건에 맞는가? or랑 같은 개념
limit= 3
ccc= [1,3,6,5]
print(any(n<limit for n in ccc))

# all : 모든 요소가 조건에 맞아야 True
print(all(n<limit for n in ccc))

#16. 형변환 연산자들 int(), float(), str(), bool()....list(), tuple(), dict(), set()

print()
#----------------------------------------------------------------------

#[별외] 기초타입 변수와 참조타입 변수의 차이.. 그리고 조심할 점.

# 파이썬의 타입 2종류
#1. 기초 타입 : int, float, str, bool                           [ 데이터를 저장하는 변수 ]
#2. 참조 타입 : list, dic, set, object 등.. 위 4개를 제외한 전부   [ 객체의 주소를 저장하는 변수 ]

# 기초타입.. 상황
a= 10
b= a
print(a)
print(b)
print()

b= 50
print(a) # 기초변수는 값을 복사해서 주는 느낌이기에 원본에 변화가 없음
print(b)

# 참조타입.. 상황
aaa= [100, 200, 300]
bbb= aaa
print('aaa:',aaa)
print('bbb:',bbb)
print()

bbb[1]= 5000
print('aaa:',aaa) # 참조변수는 주소를 공유하기 때문에 원본에 변화가 있음

