# 조건문(control) 과제

# 1.
print('입력한 수의 절대값이 출력됩니다.')
print()
q1_input= int(input('#1_정수 입력: '))

if q1_input < 0:
    q1_input= -q1_input
    print(q1_input)
else:
    print(q1_input)
print('-'*30,'\n')

# 2.
print('입력한 2개의 숫자 중 큰 수가 출력됩니다.')
print()
q2_int_input1= int(input('#2_정수 입력1: '))
q2_int_input2= int(input('#2_정수 입력2: '))

if q2_int_input1 > q2_int_input2:
    print('더 큰 값은:',q2_int_input1)
elif q2_int_input1 < q2_int_input2:
    print('더 큰 값은:',q2_int_input2)
else:
    print(f'{q2_int_input1}은 같은 값입니다.')
print('-'*30,'\n')

# 3.
print('입력한 3개의 숫자 중 가장 큰 수가 출력됩니다.')
q3_a= int(input('#3_정수 입력1: '))
q3_b= int(input('#3_정수 입력2: '))
q3_c= int(input('#3_정수 입력3: '))

q3_max= q3_a if q3_a>q3_b else q3_b if q3_b>q3_c else q3_c
print('젤큰수:',q3_max)
print('-'*30,'\n')

# 4.
q4_input_1= int(input('#4_정수 입력1: '))
q4_input_2= int(input('#4_정수 입력2: '))

if q4_input_1>q4_input_2:
    print(f'{q4_input_1} - {q4_input_2} = {q4_input_1-q4_input_2}')
elif q4_input_2>q4_input_1:
    print(f'{q4_input_2} - {q4_input_1} = {q4_input_2-q4_input_1}')
print('-'*30,'\n')

# 5.
q5_input_1= int(input('#5_정수 입력1: '))
q5_input_2= int(input('#5_정수 입력2: '))
print()
q5_result= q5_input_1-q5_input_2 if q5_input_1>q5_input_2 else q5_input_2-q5_input_1
print(q5_result)

# 6.
q6_saved_id= 'python'
q6_saved_pw= '1234'
q6_input_id= input('ID 입력: ')
q6_input_pw= input('PW 입력: ')

if q6_input_id.lower().replace(' ','') == 'python' and q6_input_pw.strip().replace(' ','') == '1234':
    print('로그인 성공!')
else:
    print('로그인 실패')
print('-'*30,'\n')

# 7.
q7_input= int(input('#7_점수 입력:'))

if 80<= q7_input <= 100:
    print('높음')
elif 50<= q7_input <80:
    print('보통')
elif 0<= q7_input <50:
    print('낮음')
else:
    print('범위를 벗어남')
print('-'*30,'\n')

# 8.
q8_str_input= input('#8_채팅 입력: ')

if 'error' in q8_str_input or '에러' in q8_str_input:
    print('XXXXX!!!Error!!!XXXXX')
else:
    print('정상입니다.')
print('-'*30,'\n')

9.
q9_int_input_1= float(input('#9_정수 입력1: '))
q9_int_input_2= float(input('#9_정수 입력2: '))
q9_int_input_3= float(input('#9_정수 입력3: '))

q9_int_input_max= q9_int_input_1 if q9_int_input_1>q9_int_input_2 else q9_int_input_2 if q9_int_input_2>q9_int_input_3 else q9_int_input_3
q9_int_input_total= q9_int_input_1+q9_int_input_2+q9_int_input_3
q9_int_input_average= q9_int_input_total/3

print('3개 중 가장 큰 수는 {}입니다.'.format(q9_int_input_max))
print('3개 수의 평균값은 {}입니다.'.format(q9_int_input_average))
if '.' in str(q9_int_input_average) :
    print('평균값이 실수입니다.')
else:
    print('평균값이 정수입니다.')