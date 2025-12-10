# 2장 -----------------------[직접해보는 손코딩 p.115]----------------------------
# 원의 둘레와 넓이 구하기 
# 변수 선언과 할당
pi=3.14159265
r= 10

# 변수 참조
print("원주율=", pi)
print("반지름=", r)
print("원의 둘레=", 2 * pi * r) #원의 둘레
print("원의 넓이=", pi * r *r) #원의 넓이
print()

# -----------------------[직접해보는 손코딩 p.120]--------------------------------
# 입력 자료형 확인하기
# 입력받기.
string= input("자료형을 확인하세요> ")
# 출력하기.
print("자료: ",string)
print("자료형: ", type(string))
print()

# 입력받고 더하기
# 입력 받기
string= input("정수 입력> ")
# 출력하기.
### print("입력+100",string+100) # TypeError
print("입력+100", int(string)+100)
print()

# int()함수 활용하기 / p.121
string_a= input("정수 입력A> ")
int_a=int(string_a)

string_b = input("정수 입력B> ")
int_b = int(string_b)

print("문자열 자료:",string_a+string_b)
print("숫자 자료:",int_a+int_b)
print()

# int() 함수와 float()함수 활용하기 / p.122
output_a= int("52")
output_b= float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)
print()

# int() 함수와 float()함수 조합하기
input_a = flooat(input("첫 번째 숫자> "))
input_b = flooat(input("두 번째 숫자> "))

print("덧셈 결과:",input_a+input_b)
print("뺄셈 결과:",input_a-input_b)
print("곱셈 결과:",input_a*input_b)
print("나눗셈 결과:",input_a/input_b)

# str()함수를 사용해 숫자를 문자열로 변환하기 / p.124
output_a=str(52)
output_b=str(52.273)
print(type(output_a), output_a)
print(type(output_b), output_b)

# --------------------[직접해보는 손코딩 p.125]---------------------
# inch단위를 cm단위로 변경하기
# 숫자 입력받기.
raw_input=input("inch 단위의 숫자를 입력하세요: ")
inch=int(raw_input)
cm=inch*2.54

# 출력하기.
print(inch, "inch는 cm단위로", cm,"cm입니다.")


