# 6.
# 2차원 좌표값은 튜플(x, y) 형태의 데이터를 사용합니다. 
# point1 = (2, 3) 
# point2 = (5, 7) 
# 1. point1의 x좌표만 출력하시오. 
# 2. point2의 y좌표만 출력하시오. 
# 3. 두 좌표 간의 거리(유클리드Euclidean 거리)를 계산하시오.[ML 유사도 계산에 사용되는 거리값]

point1 = (2, 3)
point2 = (5, 7)

print(f'{point1}의 x좌표 값: {point1[0]}')
print(f'{point2}의 y좌표 값: {point2[1]}')

po1= (point1[0]-point2[0])**2
po2= (point1[1]-point2[1])**2

result= (po1+po2)**0.5
print('두 좌표간의 거리: {:.2f}'.format(result))

