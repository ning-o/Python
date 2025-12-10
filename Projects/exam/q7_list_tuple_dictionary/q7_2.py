# 2.
# 사용자로부터 정수형 숫자 하나를 입력받자. 입력된 숫자 만큼 사용자로 부터 문자열을 입력받아 리스트에 저장하도록 해보자. 
# 입력된 문자열들이 잘 저장되어 있는지 확인하기 위해 배열의 각 요소들을 for in 반복문으로 차례로 출력해보자.

q2_int_input= int(input('#2.정수 입력> '))
q2_list= []
print()

for q2_i in range(q2_int_input):
    q2_str_input= input('#2.문자 입력> ')
    q2_list.append(q2_str_input)
print(q2_list)
print()
