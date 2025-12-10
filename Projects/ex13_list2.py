# 리스트를 생성하는 특별한 문법 [리스트 내포 list comprehensions]
# 반복문으로 리스트의 요소를 만들때 한줄로 간결하게 만들 수 있는 문법

#1_ 기존 방식대로 반복문으로 리스트 생성
aaa= [] #빈 배열

for n in range(1,10): #1~9까지
    aaa.append(n)
print(aaa)    

bbb= [n for n in range(1,10)]
print(bbb)

ccc= [n*10 for n in range(1,10)] #반복문에는 안되지만 comprhensions에서는 연산식 사용 가능
print(ccc)

ddd= [n**2 for n in range(1,10)]
print(ddd)
# 추가..문법) 기존 리스트의 값 중 특정 조건을 통과한 값만으로 새로운 리스트를 만들 수 있음.
scores=[70,80,95,442,68,73,57,84]
# 60점 미만을 걸러내고 새로운 리스트 생성
# eee= []
# for score in scores:          # 원래 방법
#     if score>=60:
#         eee.append(score)

eee= [ score for score in scores if score>=60 ] # 실제 데이터분석이나 ML작업할때 필터링을 위해 자주 활용되는 문법
print(eee)

# 사용자의 입력된 숫자만큼 빈 리스트의 요소를 만들기.. 단, 리스트의 초기값은 0으로..
num= int(input('개수:'))
ggg= [0 for n in range(num)]
print(ggg)

# 가장 쉽게 순차적인 값을 가지는 리스트 생성 방법 - 리스트를 만들어주는 함수 list()

for v in [1,2,3,4,5]:   #이거랑
    print(v)

for v in range(1,6):    #이거는 같은 게 아님
    print(v)

hhh= [1,2,3,4,5]

ggg= range(1,6)         #리스트처럼 전혀 나오지 않음.
print(ggg)

kkk= list(range(1,6))   #레인지 돌리는 숫자를 리스트로 바로 만들어줌
print(kkk)
#---------------------------------------------------------------------------------

print()
# 리스트를 다룰는 특별한 문법과 기능함수들..

#1] 리스트나 튜플의 요소들 중 최소값,최대값,합계를 구해주는 함수
score_list= [48,100,85,72,64,23,5,18]
print('최소값:', min(score_list))               #최소값
print('최대값:', max(score_list))               #최대값
print('최소값:', sum(score_list))               #총합
print('평균:', sum(score_list)/len(score_list)) #평균

# min, max는 리스트가 아니여도 가능
# print(max(10,20,30,40,50))
# 그러나 sum은 불가능
# print(sum(10,20,30,40,50)) -- error

# 딕셔너리는? key를 계산함.. 즉.. 원하는 값을 계산하지 않음.. 그래서 사용안함
aaa= {'a':10,'b':20,'c':30}
print(min(aaa))
print()

#2] 리스트나 튜플을 for 반복할때 인덱스번호화 값을 동시에 주는 함수 enumerate()
aaa= ['sam','robin','hong','park']
for value in aaa:   #값만 줌
    print(value)
print()

for idx, value in enumerate(aaa):   # 인덱스 번호도 같이 얻고 싶다면, enumerate() 함께 사용
    print(idx+1,":",value)
print()

#3] 요소의 순서를 뒤바꾸는 함수 reversed() -- 원본 리스트는 변경되지 않고.. 뒤바뀐 새로운 배열을 리턴해줌.
aaa= [10,20,30,40,50]
bbb= reversed(aaa) # aaa리스트의 요소 위치를 바꾸어 새로운 리스트를 만들어주는 녀석(객체)줌. ~마치 range()같은..
print(aaa)
print(bbb) # 이렇게는 나오지 않음
# range처럼 반복문을 사용하면.. 뒤바뀐 요소를 줌
for v in bbb:
    print(v)
# for문 사용이 싫다면.. 리스트로 만들기.
ccc= list(reversed(aaa))
print(ccc)

# 혼동하기 쉬운 리스트의 기능함수..
aaa.reverse() # 리스트의 기능임.. 이것은 원본 리스트의 순서가 바뀜 .reverse()
print(aaa)


# stu1= {'name':'홍길동','score':70,'num':31,'gender':'male'}
# stu2= {'name':'유길동','score':90,'num':1,'gender':'male'}
# stu3= {'name':'고길동','score':40,'num':20,'gender':'male'}
# stu4= {'name':'김길순','score':10,'num':11,'gender':'female'}

# for student in stu1:
#     for student2 in student:
#         print(student,stu1[student])
#         print(student2,stu2[student2])


# python 3버전 이상에서 완전 도입된 {set:집합} 자료형
aaa= {10,20,30,40,40,20,50} #중복된 값이 저장되지 않음. 순서대로 저장되지 않음.
print(aaa)

for v in aaa:
    print(v)

bbb= [10,203,50,50]
ccc= set(bbb)

# set의 주요연산자.. (과제에 나오니 검색으로 해결)
# 합집합 : | 또는 .union()
# 교집합 : & 또는 .intersection()

# 두 집합(set)안에 요소들 중 
