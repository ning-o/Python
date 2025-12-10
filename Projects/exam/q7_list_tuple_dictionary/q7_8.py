# 8.
# 입력값들의 분포를 시각적으로 볼 수 있는 히스토그램을 만드는 프로그램을 작성하시오. 
# 이 프로그램은 1부터 100이하의 정수 10개를 읽어야 하고, 1-10,11-20 등의 범위에 드는 값들의 횟수를 아래와 같이 출력하여야 한다. 
#  1 - 10 : **** 
# 11 - 20 : ** 
# 21 - 30 : * 
# 31 - 40 : ** 
# .......... 
# .......... 
# .......... 
# 91 -100 : *

number= []

for q8_a in range(10):
    num= int(input(f'{q8_a+1}번째 정수 입력> '))
    if 1 <= num <= 100:
        number.append(num)
    else:
        print('잘못된 값입니다.')
bin= [0]*10

for num in number:
    idx=(num-1)//10
    bin[idx]+=1

for q8_c in range(10):
    start= q8_c*10+1
    end= (q8_c+1)*10
    stars = '*' * bin[q8_c]
    print(f'{start:2d} - {end:3d} : {stars}')

    