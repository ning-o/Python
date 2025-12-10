# for 반복문과 범위   p.234

for i in range(5):
    print(str(i)+'=반복 변수')
print()

for i in range(5,10):
    print(str(i)+'=반복 변수')
print()

for i in range(0,10,3):
    print(str(i)+'=반복 변수')
print()

# 리스트와 범위를 조합해서 사용하기
array= [273,32,103,57,52]

for i in range(len(array)):
    print("{}번째 반복:{}".format(i, array[i]))
print()

# 반대로 반복하기
for i in range(4,0 - 1,-1):
    print('현재 반복 변수: {}'.format(i))
print()
for i in reversed(range(5)):
    print('현재 반복 변수: {}'.format(i))

# 반복문으로 피라미드 만들기
# star= ''
# for a in range(1,10):
#     for b in range(0,a):
#         star += '*'
#     star += '\n'
# print(star)

# 반복문으로 피라미드 만들기2
star=""
for a in range(0,15):
    for b in range(15,a,-1):
        star+= ' '
    for c in range(0,2*b-1):
        star+= '*'
    star += '\n'
print(star)

# while 반복문을 for 반복문처럼 사용하기
i=0
while i<10:
    print(f'{i+1}번째 반복입니다.')
    i += 1


