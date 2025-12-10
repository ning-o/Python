# Tuple () --리스트와 비슷한데.. 요소의 값변경/추가/삭제 불가능 (immutable)

bbb= (10,20,30)
print(bbb)
print(type(bbb))


# 요소값 사용하는 방법은 같음- 인덱스 번호
print(bbb[0])
print(bbb[1])
print(bbb[2])
print()

# 값변경..요소추가..삭제 모두 불가능
#bbb[0]= 100 --error
# bbb.append(50) --error
# bbb.remove(20) --error

for value in bbb:
    print(value+1)
print()

# 특이하게 튜플 생성 방법.. 권장은 하지 않음
bbb= 10,20,30 # 이렇게 쓰면 파이썬이 알아서 튜플로 만들어버림
print(bbb)
print(type(bbb))
print()

# 반대로 튜플의 요소값들을 여러개의 변수로 분리해서 대입하는 것이 가능(ML머신러닝 작업할때 애용)
bbb= (10,20,30)
print(bbb[0])
print(bbb[1])
print(bbb[1])
print()

a,b,c= bbb # 요소들이 분해돼서 각 변수에 대입됨 # 리스트도 가능
print(a)
print(b)
print(c)

a,b,c= (10,20,30) # 위와 같은 개념

#z,x= (10,20,30) #error.. 개수가 다르면 에러..

# 튜플은 원본데이터를 실수로라도 건드리지 못하도록 할때 유용하게 사용됨.
# 안전하게 데이터를 다룰 수 있다는 장점
