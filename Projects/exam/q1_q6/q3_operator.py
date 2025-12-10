# 연산자 [operator] 과제

# 1.
print('입력한 두 수의 몫과 나머지가 출력됩니다.')
print()

q1_input1= int(input('숫자 입력1: '))
q1_input2= int(input('숫자 입력2: '))

quota= q1_input1//q1_input2
rest= q1_input1%q1_input2

print(f"{q1_input1}과{q1_input2}의 몫은 {quota}입니다.")
print(f"{q1_input1}과{q1_input2}의 나머지는 {rest}입니다.")
print('-'*30,'\n')

# 2.
print('반지름을 입력하면 면적이 출력됩니다.')
print()

pi= 3.141592
r= float(input('반지름 입력: '))

q2_result= pi*r*r

print(f'원의 면적은 {'{:.2f}'.format(q2_result)}입니다.')
print()

# 3.
print('원화를 달러로 환산하여 출력됩니다.')
print()

won= int(input('원화를 입력하세요: '))
dollar= won/1450
print(f'{won}원은 {'{:.2f}'.format(dollar)}달러 입니다.')
print()

# 4.
print('입력한 3개의 수의 평균값이 출력됩니다.')
print()

q4_output1=int(input('값 입력1: '))
q4_output2=int(input('값 입력2: '))
q4_output3=int(input('값 입력3: '))

q4_result= (q4_output1+q4_output2+q4_output3)/3

print(f'{q4_output1} {q4_output2} {q4_output3}의 평균값은 {'{:.2f}'.format(float(q4_result))}입니다.')
print()

# 5.
print('시간을 입력하면 00시 기준으로 몇 초가 흘렀는지 계산해줍니다.')
print()

q5_input_h= int(input("시 입력: "))
q5_input_m= int(input("분 입력: "))
q5_input_s= int(input("초 입력: "))

hour= q5_input_h*60*60
min= q5_input_m*60
q5_result= hour+min+q5_input_s

print('{:d}초 경과 되었습니다.'.format(q5_result))
print()

# 6.
print('받은 돈을 입력하면 부가세와 잔돈이 출력됩니다.')
print()

q6_input1= int(input('받은 돈: '))
q6_input2= int(input('상품 가격: '))

tex= q6_input1/10
change= q6_input1-q6_input2-tex

print(f'''부가세: {'{}'.format(int(tex))}
거스름 돈: {'{}'.format(int(change))}''')
print()

# 7.
print('직사각형의 넓이를 구하는 프로그램입니다.')
print()

q7_input_x1= int(input('좌 상단의 x좌표: '))
q7_input_y1= int(input('우 상단의 y좌표: '))
q7_input_x2= int(input('좌 하단의 x좌표: '))
q7_input_y2= int(input('우 하단의 y좌표: '))

width= q7_input_x1-q7_input_x2
length= q7_input_y1-q7_input_y2

print(f'직사각형의 넓이는 {width*length}입니다.')

# 문자열 연산자 과제
# 1.
print()
q1_1_input1= str(input('첫번째 문자를 입력하세요: '))
q1_1_input2= str(input('두번째 문자를 입력하세요: '))
q1_1_input3= q1_1_input1+q1_1_input2

print(f'{q1_1_input1+q1_1_input2} {q1_1_input3*3}')
print()

# 2.
# 정해진 변수에서 'Python'만 추출하세요

# 정해진 변수
sentence= 'I love Python programming'
print(sentence[7:13])