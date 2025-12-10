#-------------------------------------[p.135]-----------------------------------------------
# format() 함수로 숫자를 문자열로 변환하기
string_a='{}'.format(10)

print(string_a)
print(type(string_a))
print()

# format() 함수의 다양한 형태       --p.136
# format() 함수로 숫자를 문자열로 변환하기
format_a= '{}만 원'.format(5000)
format_b= '파이썬 열공하여 첫 연봉 {}만 원 만들기'.format(5000)
format_c= '{} {} {}'.format(3000,4000,5000)
format_d= '{} {} {}'.format(1,'문자열',True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)
print()

# 정수를 특정 칸에 출력하기         --p.137
# 정수
ouput_a= "{:d}".format(52)

# 특정 칸에 출력하기
output_b= "{:5d}".format(52)     #5칸
output_c= "{:10d}".format(52)    #10칸

output_d= "{:05d}".format(52)   #양수
output_e= "{:05d}".format(-52)  #음수
print()

print("# 기본")
print(ouput_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)
print()


# 기호 붙여 출력하기        --p.138
output_f= "{:+d}".format(52)    #양수
output_g= "{:+d}".format(-52)   #음수
output_h= "{: d}".format(52)    #양수:기호 부분 공백
output_i= "{: d}".format(-52)   #음수: 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print()

# 조합해보기                --p.139
output_h= "{:+5d}".format(52)       #기호를 뒤로 밀기: 양수
output_i= "{:+5d}".format(-52)      #기호를 뒤로 밀기: 음수
output_j= "{:=+5d}".format(52)      #기호를 앞으로 밀기: 양수
output_k= "{:=+5d}".format(-52)     #기호를 앞으로 밀기: 양수
output_l= "{:=+05d}".format(52)     #0으로 채우기: 양수
output_m= "{:=+05d}".format(-52)    #0으로 채우기: 음수

print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print()

# 다양한 형태읭 부동 소수점 출력하기        --p.140
output_a= "{:f}".format(52.273)         
output_b= "{:15f}".format(52.273)       #15칸 만들기
output_c= "{:+15f}".format(52.273)      #15칸에 부호 추가하기
output_d= "{:+015f}".format(52.273)     #15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

# 소수점 아래 자릿수 지정하기
output_a= "{:15.3f}".format(52.273)
output_b= "{:15.2f}".format(52.273)
output_c= "{:15.1f}".format(52.273)
output_d= "{:015f}".format(52.273)
output_e= "{:015.2f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print()

# 의미없는 소수점 제거하기
output_a= 52.0
output_b= "{:g}".format(output_a)
print(output_a)
print(output_b)

# ---------------------------------------------------------
# 구의 부피와 겉넓이를 구하는 프로그램 만들기.
pi= 3.141592
r= float(input('구의 반지름을 입력해주세요: '))

vol= (4/3) * pi * (r**3)
outer_area= 4* pi * (r**2)

print(f"= 구의 부피는 {"{:.2f}".format(vol)}입니다.")
print(f"= 구의 겉넓이는 {"{:.2f}".format(outer_area)}입니다.")

# 피타고라스의 정리

a= int(input("밑변의 길이를 입력해주세요: "))
b= int(input("높이의 길이를 입력해주세요: "))

c= (a**2+b**2)**(1/2)
print(f"빗변의 길이는 {"{:.2f}".format(c)}입니다.")