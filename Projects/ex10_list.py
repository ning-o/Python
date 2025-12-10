# 배열{Array} 파이썬에서 대량의 데이터를 다루는 문법 [ List, Tuple, Dictionary, {Set} ]

# 배열안에 개별 데이터(칸 하나의 값)를 '요소{eleement}'라고 한다. ex) aaa=[10,20,30] --10,20,30이 요소들
# 요소들의 개별 고유 번호를 '인덱스{index}'번호라고 한다. ex) aaa=[10,20,30] --aaa[0]은 10의 인덱스 번호

#1. List [] - 요소 값 변경 및 추가/삭제 가능
aaa= [10, 20, 30, 40]
#리스트를 저장한 변수를 출력하면 그 안에 있는 값들을 모두 보여줌
print(aaa)
print(type(aaa)) #자료형 확인하기

# 요소값 개별사용 - 인덱스 번호
print(aaa[0])
print(aaa[1])
print(aaa[2])
print(aaa[3])
#print(aaa[4]) -- IndexError>> list index out of range
print()

# 요소의 개수가 만ㄶ으면.. 인덱스 번호를 찾기 어려워짐.. 반복문으로 인덱스 번호를 자동으로 증가되도록..
for n in range(4): # 0,1,2,3
    print(aaa[n])
print()

# for 문법의 대량의 데이터에서 요소를 반복적으로 뽑아오는 것임.
# 인덱스 번호를 뽑지말고.. 바로 aaa리스트의 요소를 뽑으면 더 간단하다.
for e in aaa: #더 간단하지만 역순 출력은 할 수 없음.
    print(e)
print()

for n in range(3,-1,-1): # 역순 출력 방법1
    print(aaa[n])
print()

for n in range(4): # 역순 출력 방법2
    print(aaa[3-n])
print()

# 1~3번 방의 요소만 출력. [범위 출력]
for n in range(1,4):
    print(aaa[n])
print()

# 2번만 건너뛰고 출력.
for n in range(4):
    if n ==2: continue
    print(aaa[n])

# 모든 요소값들에 1을 더한 값을 출력하세요.. 요청
for n1 in aaa:
    print(n1+1)
print()

# 모든 요소값을 더한 총합 계산도 가능
# total= aaa[0]+aaa[1]+aaa[2]+...
total=0
for n2 in aaa:
    total= total+n2
print('총합:',total)

sum(aaa)

# 리스트의 요소들 중에서 가장 큰 값 출력.
# if aaa[0]>aaa[1] and aaa[0]>aaa[2] and aaa[0]>aaa[3]:
#     m=aaa[0]
# elif aaa[1]>aaa[2] and aaa[1]>aaa[3]:
#     m=aaa[1]
# elif aaa[2]>aaa[3]:
#     m=aaa[2]
# else:
#     m= aaa[3]

m= aaa[0]
if m<aaa[1]: m= aaa[1]
if m<aaa[2]: m= aaa[2]
if m<aaa[3]: m= aaa[3]
print(m)

m= aaa[0]
for n in range(1,4):
    if m<aaa[n]: m= aaa[n]
print(m)

max(aaa)
print()

# 요소값 변경 - 인덱스 번호 사용
aaa[0]= 100
print(aaa)

# 요소를 추가 - append(), insert()
#aaa[4]= 50 --error(자바스크립트에서는 가능)
aaa.append(50) # 50이라는 값을 리스트의 '마지막'에 추가
print(aaa)

print(aaa[2])
aaa.insert(1, 600) # 1번 인덱스 위치에 600이라는 값을 삽입 
print(aaa)

print(aaa[2]) # 인덱스 번호도 재조정됨.

# 요소 삭제 - remove(), clear() --기능, del --연산자
aaa.remove(100) # 100이라는 값을 가진 요소를 제거
print(aaa)

del aaa[2] # aaa[2] 요소를 제거
print(aaa)

aaa.clear() # 모두 삭제
print()

# 요소의 개수를 알려주는 파이썬의 내장 기능 함수 len()
print('요소 개수:',len(aaa))

# 요소들의 자료형이 달라도 상관없음.
aaa= [10, 3.14, False, 'sam']
print(aaa)

# 반복문으로도 접근 가능
for e in aaa:
    print(e)
print()

# 리스트가 가진 유용한 여러 기능함수들 소개..
#1) 요소의 순서를 뒤집기
aaa.reverse() # 원본 리스트가 변경됨.
print(aaa)

#2) 요소 정렬
aaa= [4,15,7,2,16,4,10]
aaa.sort()
print(aaa)

#3) 요소 중 특정 값의 인덱스 번호(위치) 얻어오기
idx= aaa.index(16)
print(idx)

#4) 특정값이 리스트안에 있는지 여부.. in 연산자
print( 7 in aaa )
print( 70 in aaa )
print( 5 not in aaa ) # 있지않니? == 없냐?

#5) 특정값이 리스트안에 몇개인지..
print( aaa.count(4) ) # 4라는 숫자가 몇개 있니

#6) 특정값 꺼내오기.. -- 원본에서 없어지는 것
n= aaa[2] # 이건 꺼내온 게 아니고 사용한 것 (immutable)
print(n)
print(aaa) # 여전히 리스트 안에서도 존재

n= aaa.pop(2)   # 이건 꺼내온 것
print(aaa)      # 원본에서 사라짐 (mutable)

#7) 다른 리스트를 한방에 추가하기.. [리스트의 확장]
aaa= [10,20,30]
bbb= [4,5,6]

aaa.extend(bbb)
print(aaa)

# .extend() 기능 잘 사용안함. 왜? + 연산을 하면 리스트 확장 기능이 발동함

ccc= [700,800,900]
print(aaa+ccc)
print()

#--------------------------------------------------------------

# 2차원 리스트 -- 리스트의 요소가 또 다른 리스트
aaa= [[10, 20, 30],['aa', 'bb'],[3.14, 12.2, 300, 500]]
print(aaa)
print(aaa[0])
print(aaa[0][0])
print(aaa[1][0])

# len() 기능은.. 리스트의 요소개수를 알려줌
print(len(aaa))
print(len(aaa[0]))
print(len(aaa[1]))
print(len(aaa[2]))
print()

# 각 요소값들 접근..하여 사용
print(aaa[0][0], end='\t')
print(aaa[0][1], end='\t')
print(aaa[0][2], end='\t')
print()

print(aaa[1][0], end='\t')
print(aaa[1][1], end='\t')
print()

print(aaa[2][0], end='\t')
print(aaa[2][1], end='\t')
print(aaa[2][2], end='\t')
print(aaa[2][3], end='\t')
print()

print()

# 위 작업을 반복문으로 줄이기.
for n in range(len(aaa[0])): 
    print(aaa[0][n], end= '\t')
print()

for n in range(len(aaa[1])):
    print(aaa[1][n], end= '\t')
print()

for n in range(len(aaa[2])):
    print(aaa[2][n], end= '\t')
print()

# 각 줄을 출력하는 3개의 덩어리를 반복문으로 줄이기.
for k in range(len(aaa)): 
    a= len(aaa[k])
    for n in range(a):
        print(aaa[k][n], end= '\t')
    print()
print()

print()

#[row:행(줄), column:열(칸)]
for row in aaa:
    for column in row:
        print(column, end='\t')
    print()
print()
#--------------------------------------------------------------------
print()

# 리스트를 사용하여 여러데이터를 다루는 예제.. 2개
# ex1) 학생 성적의 총합과 평균
score_list= [80,75,64,90,50]
total= 0
for score in  score_list:
    total= total+score
print('총점:',total)
print('평균:',total/len(score_list))
print()

# ex2) 일주일의 온도 중에서 가장 더운 날의 온도와 요일은? (데이터의 순서: 월,화,수,목,금,토,일)
week_temparature= [15,8,16,9,7,6,10]
highest= week_temparature[0]
for temp in week_temparature:
    if highest<temp: highest= temp
print('최고 온도:',highest)

idx= week_temparature.index(highest)
print(idx)

if idx==0:
    print('월요일')
elif idx==1:
    print('화요일')
elif idx==2:
    print('수요일')
elif idx==3:
    print('목요일')
elif idx==4:
    print('금요일')
elif idx==5:
    print('토요일')
elif idx==6:
    print('일요일')
print()
week= ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(week[idx])
#-----------------------------------------------------

