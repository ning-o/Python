# 변수(variable) 과제

# 1. 자기소개 print() 기능을 사용해 출력하기
print()

q1_name= "민수"
q1_food= "피자"

print('안녕하세요! 저는 {}입니다.'.format(q1_name))
print(f'좋아하는 음식은 {q1_food}입니다.')
print("-"*30,"\n")

# 2. 변수로 문장 만들기

q2_name= "홍길동"
q2_age= 20
q2_hobby= "game"

print(f'제 이름은 {q2_name}이고, 나이는 {q2_age}살입니다.\n제 취미는 {q2_hobby}입니다.')
print("-"*30,"\n")

# 3. 자료형 확인하기.

q3_name = "철수"
q3_age = 15
q3_height = 165.3
is_q3_student = True

print(type(q3_name),q3_name)
print(type(q3_age),q3_age)
print(type(q3_height),q3_height)
print(type(is_q3_student),is_q3_student)
print("-"*30,"\n")


# 4. 간단한 계산기 만들기
q4_num1 = 10
q4_num2 = 3

print(f'{q4_num1}+{q4_num2}={q4_num1+q4_num2}')
print(f'{q4_num1}-{q4_num2}={q4_num1-q4_num2}')
print(f'{q4_num1}*{q4_num2}={q4_num1*q4_num2}')
print(f'{q4_num1}/{q4_num2}={q4_num1/q4_num2}')
print("-"*30,"\n")

# 5. 변수 활용 문장 완성하기

country= "한국"
city= "서울"
year = 2025

print(f"{year}년에 저는 {country} {city}에 살고 있습니다.")
print("-"*30,"\n")

# 키보드 입력: input() 과제

# 6. 사용자로부터 2개의 정수를 입력받아 뺄세메과 곱셈의 결과를 출력하는 프로그램
print("정수 두개를 입력하면 덧셈과 뺄셈을 출력합니다.")
print()

q6_num1=input("정수 입력1: ")
q6_num1=int(q6_num1)

q6_num2=input("정수 입력2: ")
q6_num2=int(q6_num2)

print(f"{q6_num1} + {q6_num2} = {q6_num1+q6_num2}")
print(f"{q6_num1} - {q6_num2} = {q6_num1-q6_num2}")
print("-"*30,"\n")

# 7. 
print("[숫자1] x [숫자2] + [숫자3] = 을 계산해주는 프로그램입니다.")
print()

q7_num1=input("숫자 입력1: ")
q7_num1=int(q7_num1)

q7_num2=input("숫자 입력2: ")
q7_num2=int(q7_num2)

q7_num3=input("숫자 입력3: ")
q7_num3=int(q7_num3)

print(f'{q7_num1} * {q7_num2} + {q7_num3} = {q7_num1*q7_num2+q7_num3}')
print("-"*30,"\n")

# 8.
print('입력한 수의 제곱 값이 출력됩니다.')
print()

q8_num=input('숫자를 입력하세요: ')
q8_num=int(q8_num)

print(f'{q8_num}의 제곱은 {q8_num**2}입니다.')
print("-"*30,"\n")

# 9.
print('입력한 두개의 실수의 사칙연산 값이 출력됩니다.')
print()

q9_num1=input('실수 입력1: ')
q9_num1=float(q9_num1)

q9_num2=input('실수 입력2: ')
q9_num2=float(q9_num2)
print()
print(f'{q9_num1} + {q9_num2} = {q9_num1+q9_num2}')
print(f'{q9_num1} - {q9_num2} = {q9_num1-q9_num2}')
print(f'{q9_num1} * {q9_num2} = {q9_num1*q9_num2}')
print(f'{q9_num1} / {q9_num2} = {q9_num1/q9_num2}')
print("-"*30,"\n")

# 10.
print('마일을 킬로미터로 변환하여 출력합니다.')
print()

q10_num=input('마일을 입력하세요: ')
q10_num=float(q10_num)

km=q10_num*1.69

print(f"{int(q10_num)}마일은 {km}킬로미터 입니다.")
print()

