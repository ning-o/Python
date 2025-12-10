# 연산자(Operator) : 산술, 비교, 논리, 비트, 복합대입, 형변환

# 1. 산술
a= 10
b= 4

print( a + b )
print( a - b ) 
print( a * b )
print( a / b )

print( a % b ) # 나머지 연산자
print( a // b ) # 몫

# ex1) 나머지 연산자 활용 예시 (시험지 홀짝 프로그램)

### no= int(input('수험번호 입력: '))
### if no%2==1:
###     print("홀수")
### else:
###     print("짝수")

# ex2) 그 숫자의 1의 자리 값을 뽑아오기.
### n_1= no%10
### print(n_1) # 3자리 이상 숫자에서 1의 자리만 뽑아낼 수 있다.

### n_100= no//100
### print(n_100)

# 나눗셈의 몫, 나머지 값을 한번에 연산하여 결과를 주는 기능함수를 제공함. divmod()
x, y= divmod(a,b)
print('몫: ',x)
print('나머지: ',y)

# 부호 변경 연산자 - [단항 연산자]
c= 10
print(-c) # 출력: -10 (음수>양수로 변경)

c= -10
print(-c) # 출력: 10 (양수>음수로 변경)

# 제곱연산 연산자
a= 4
print(a**2) #4의 제곱
print(a**3) #4의 3제곱
print(a**(1/2)) #4의 제곱근(루트)
print()

# 2. 비교 연산자
a=10
b=4

print(a>b) #True
print(a<b) #Flase
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

# a 변수가 특정 범위안에 있는지.. 여부
# a가 0~100 사이의 숫자인가..
print(0<a<100)

#나이가 20대 인가요?
age= 25
print(20<=age<30)

# 3. 논리 연산자 : and, or, not
# 하나의 변수에 대한 범위 조건이 아니라.. 2개 변수의 조건을 동시에 체크하는 경우도 많음.
# ex) 놀이기구 탈때.. 나이가 10살 이상이고.. 키가 150이상인 조건만 허용..
age= 15
height= 160

print(age>=10 and height>=150) # 두 비교연산의 결과가 모두 True인 경우만. True가 되는 논리연산

# 나이가 10살 미만이거나, 키가 150보다 작다면..
print(age<10 or height<150) # 두 비교 연산의 결과 중 하나라도 True면 True 결과를 주는 논리연산

# 미성년자가 아닙니까?
### print(age>=20) # 성인입니까?
print(not age<20) # 미성년자가 아닙니까? (위와 결과는 같음)
print()

# 4. 비트 연산자 (거의 사용 안함. 한번만 살펴보기..)
# 연산에 사용된 피연산자들을 2진수로 바꾸어.. 각 비트자리끼리 연산수행
# 비트 연산자는 기본적으로 2진수 연산자
print(7&4) # and 비트연산 [직렬연산: 둘다 ON이여야 ON]
print(7|4) # or 비트연산 '|' = 파이프라인 기호 [병렬연산: 둘 중 하나만 ON이여도 ON] 
print(7^4) # exclusive or 비트연산
print(8>>2) # shift 연산.. 비트를 오른쪽으로 2칸 밀기(1000==>0010)
print(8<<2) 
print(~10) # 반대 연산.. 0->1, 1->0 (숫자의 부호도 바뀌어버림)

# 5. 복합대입연산자 (산술+대입)
# a변수가 갖진 값을 1 증가시켜라.. 요청
### a= int(input('입력: '))

a=10
a+1 #덧셈은 하지만.. 그 결과가 a변수에 대입되진 않음.
print('a: ',a)
# 증가되려면.. 연산한 결과를 다시 a변수에 대입해야 함.
a=20
a= a+1
print('a: ',a) #21

a= a+2
print('a: ',a) #23

a= a+10
print('a: ',a) #33

# 변수명을 2번씩 쓰는 게 불편해서..
character_age=20
character_age = character_age +1
print(character_age)

character_age += 1
print(character_age)

character_age += 5
print(character_age)

character_age -= 3
print(character_age)

character_age *= 10
print(character_age)

character_age /= 2
print(character_age)
print()

# 6. 형변환 연산자 [type casting]
a= '10'
print(type(a))
### print(a+3) # error : str + int
# '10' --> 10 변환하기
a= int(a) # integer:정수(소수점이 없는 수)
print(type(a))
print(a+3) # int로 형변환했기 때문에 error가 나지않음.

a= '3.14'
### print(int(a)+5.14) #error : int는 정수만
a= float(a) # float:실수(소수점이 있는 수)
print(a+5.12)

# str() 형변환 기능. -- 문자열로 전환
print(5+3) # 숫자+숫자 는 산술 더하기
print(str(5)+str(3)) # 문자+문자 는 문자열 결합 연산 '5'+'3'='53'

# bool() : 단순히 "True" 문자열을 True 논리값으로 변환하는 것은 아님.
# 파이썬은 값이 없는 것(0, "", [], None, False)을 제외하고 모두.. 참(True)
a= 'True'
print(type(a))

a= bool(a)
print(type(a))

a=10
print(bool(a)) # True

a=0
print(bool(a)) # False

a=-5
print(bool(a)) # True

a="Hello"
print(bool(a)) # True

a=""
print(bool(a)) # False

a=" "
print(bool(a)) # True, 공백 문자도 문자임

a=None
print(bool(a)) # False

a=0.0
print(bool(a)) # False

# 나중에 조건문 if 문법을 사용할때 조건에 대해 확인할때.. 이 개념을 사용함.

# 일반 산수에도 연산자 우선순위가 있듯이.. 파이썬에도 존재함.
print(3+5*6) # +보다 *를 우선 연산..
print((3+5)*6) # 우선순위 변경은 소괄호..

num= 3+6 # = 대입 연산자가 우선순위 중 제일 최하위

print("-"*30,'\n')

# 프로그램에서 사용하는 대부분의 데이터는 문자열이 많음 [이름, 제목, 메모글, 리뷰, 아이디]
# 문자열 데이터를 다루기 위한 연산자와 기능함수들.. 소개

# 1) 문자열 연산자 3개  +    *   []
# 1] + 결합 연산자
print('aa'+'bb')
# 2] * 반복 연산자
print('aa'*3) #aa를 3번 반복하여 문자열 생성
s='Good'*5 #==>"GoodGoodGoodGoodGood" 
print(s)
### print('aa'-'bb') --error
### print('aa'-'bb') --error

# 3] []문자열에 인덱싱.. 슬라이싱
s= 'Hello world'
print(s)
# 문자열(문자가 여러개인 것..)의 특정 위치 글자를 뽑아올 수 있음.
print(s[1])     # 인덱스 번호(0부터~)가 1번인 위치의 값.. 'e' 
print(s[1:7])   # 1번부터~ 7번 전까지.. [1~6]의 글씨를 뽑아오기. (끝번호를 포함하지 않음)
print(s[1:])    # 1번부터~ 끝까지
print(s[:7])    # 처음부터~ 7번 전까지.. [0~6]
print(s[-1])    # 뒤에서 첫번째 요소의 글씨(마지막 글자)..
print(s[-5])    # 뒤에서 5번째 요소의 글씨(마지막 글자)..
print(s[-5:])    # 뒤에서 5번째 요소의 글씨부터~ 끝까지
print()

# 2) 문자열이 가진 유용한 기능함수들()...

# 1] 문자열의 길이(글자수) 알려주는 내장함수 len() : length
s= "Hello world"
print(len(s))

# 2] '문자열데이터'.format() 기능 -- 특정 서식 모양을 만들어 사용하는 기능
money= 500
print(money, "만원")
print("{}만원".format(money))
name= "sam"
age= 20
print("이름: {}    나이: {}".format(name,age))
aaa="{}님 반가워요".format(name)
print('만들어진 문자열: ',aaa)
print("글자수는: ", len(aaa))

# formkat() 의 {}에 들어갈 데이터ㅓ의 종류를 미리 고정할 수 있음. 코드 실수 방지!!
print("{}   {}".format(10,'aaa')) # 숫자,문자 가능
### print("{:d}   {:d}".format(10,'aaa')) 
# ㄴd (d: decimal 10진수) 데시멀이 아닌 값을 넣었기 때문에 error. 받을 값에 제약을 검.[정수만 가능]
print("실수: {:f}".format(3.14)) #float :f
print("문자열: {:s}".format("nice")) #string :s

# 데이터를 출력할때 표시되는 칸수를 지정할 수 있음.
hour=1
min= 24
sec= 3
print("{:02d}:{:02d}:{:02d}".format(hour,min,sec))

# 정수일때.. 칸수 지정
print("[{:5d}]".format(100))    # 대괄호는 의미 없음(몇 칸 띄었는지 보기 위함.)
print("[{:05d}]".format(100))   # 앞에는 채우는 숫자는 0만 가능

# 부호가 표시되고 싶다면..
print("[{:+d}]".format(30))     # 부호를 표시하는 기호가 + 이고, 양수를 뜻하는 게 아님
print("[{:+d}]".format(-30))  

# 부호가 표시되는 영역을 비워놓고 싶다면
print("[{: d}]".format(30))
print("[{: d}]".format(-30))

# 부호를 칸의 왼쪽 끝(맨앞)으로 배치하기, 공간의 여유가 있을 때, 규격화된 표기법이 필요할 때
print("[{:=+8d}]".format(30))
print("[{:=+8d}]".format(-30))

# 실수일때..
print("{:f}".format(3.14))      # float을 쓰면 무조건 소수점 아래 6자리까지 출력됨.
print("{:10f}".format(3.14))    # 정수와 같은 개념 출력: [  3.14000000]
# 소수점 아래의 칸수를 지정
print("{:.2f}".format(3.14))    # 소수점 밑으로 2자리까지만
print("{:10.2f}".format(3.14))  # 전체 10자리이나, 소수점 밑으로 2자리까지만
# 정수를 소수점으로 표시하기
print("{:.1f}".format(100))
# 소수점이 필요하면 찍고, 아니면 찍지 않았으면 (정수인지 실수인지 모를때)
print('{:g}'.format(100))       # generator 자동
print("{:g}".format(3.14)) 

# 문자열일때..
print("이것은 {:s}입니다.".format('aaa'))
print("이것은 {:10s}입니다.".format('aaa'))     # [이것은 aaa       입니다.]
# 남은 공간의 오른쪽으로 배치..
print("이것은 {:>10s}입니다.".format('aaa'))    # [이것은        aaa입니다.]

# 진법 표시
print("{:d}".format(10))  # 10진수    - decimal
print("{:o}".format(10))  # 8진수     - octal 
print("{:x}".format(10))  # 16진수    - hexadecimal
print("{:b}".format(10))  # 2진수     - binary

# 파이썬 코드로 2진수, 8진수, 16진수를 표기해보기..
print("{:d}".format(0o10))  # 8진수 표기법 0o
print("{:d}".format(0x10))  # 16진수 표기법 0x
print("{:d}".format(0b10))  # 8진수 표기법 0b