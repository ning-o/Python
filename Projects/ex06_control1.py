# 제어문(control) -- 프로그램의 진행순서를 제어하는 문법

#1. 조건문 if, if-else, if-elif

#1) if
age= 15
if age>20:
    print('미성년자군요. 시청에 주의하세요.')
    print('다른 콘텐츠를 시청하세요.')

print('넷플릭스 입니다.')
print()
#--------------------------------------------------------

#2) if - else
age= 15
if age>=20:
    print('환영합니다. 문나이트입니다.')
    print('신나게 노세요~~')
    # 영역안에 출력기능만 사용한 것은 아님.
    # 어떤 코드든 가능.
    n= 10
    n+= 2
    print('n:',n)
else :
    print('가세요라')
    print('더 커서 와~~')
print('-'*30,'\n')

#3) 중첩 if
age= 25
if age<20:
    print('꺼져!')

    if age>18:
        print('뒷문으로..')
else:
    print('환영합니다. 문나이트 입니다.')

    gender= 'female'
    if gender== 'female':
        print('할인해줍니다.^^')
    else:
        print('정가 그대로..ㅠㅠ')
    
    print('필요한 거 있으면 "찬호박"을 찾아주세요.')
print('-'*30,'\n')

#4) if - elif - (else)
#ex)시험점수를 입력하면 학점을 계산하여 알려주는 프로그램
score= 955
if 90<= score <=100:
    print("'A'학점 입니다.") 
    print('아주 우수합니다.')
elif 80<= score <90:
    print("'B'학점 입니다.")
    print('우수합니다.')
elif 70<= score < 80:
    print("'C'학점 입니다.")
    print('준수합니다.')
elif 60<= score < 70:
    print("'D'학점 입니다.")
    print('분발하세요.')
elif 0< score <60:
    print("'F'학점 입니다.")
    print('주글께 그냥~')
else:
    print('잘못 입력했습니다.')
    print('0~100점 사이만 입력하세요.')
print('-'*30,'\n')

#5) 2개 이상의 변수 조건을 묶어서 비교해야하는 경우 -- 비교 연산을 묶어주는 [논리연산] and, or, not

#5.1) and를 사용해야하는 경우 [2개 조건 모두 충족 해야함.]
score= 95 # 점수
absent_days= 1 # 결석일수
if score>=90 and absent_days <=1:
    print("'A+'학점입니다. 성실하면서 성적도 우수합니다.. 최우수 학생입니다.")
else:
    print('최우수 학생은 아닙니다.')
print()

#5-2) or를 사용하는 경우 [2개 조건 중 하나만 충족해도 됨.]
review= '오늘 신발이 도착했어요'
review= '오늘 신발 도착했는데 완전 좋아요'
review= '오늘 신발 도착했는데 배송도 빠르고 이거 편하네요 만족합니다.'
if ('좋아요' in review) or (len(review) >= 20) :
    print('이벤트 당첨!')
else:
    print('탈락! 원하는 단어가 없거나 글자수가 너무 적어요.')
print()

#5.3) not을 사용하는 경우 [코드를 해독할때.. 사람이 생각하는대로 써져있어서 선호함]
#ex) 성인이 아니면.. 이라는 조건
age= 15
if not age>20:
    print('미성년')
else:
    print('성인')
print('-'*30,'\n')

#6) 조건에 사용하는 비교연산인 크다 작다만 있는 것은 아님. 같다 ==를 사용하는 조건
# 강아지 키우는 게임
print('---------------')
print('@ 강아지 키우기 @')
print('---------------')
print('1. 밥먹기')
print('2. 산책하기')
print('3. 목욕하기')
print('---------------')
menu= input('메뉴 선택: ')
print()

# 메뉴 선택에 따라 다른 동작..
if menu=='1' or menu== '밥먹기':
    print('와구와구... 맛있다!')
elif menu=='2' or menu== '산책하기' or menu== '산책':
    print('와우~~~ 씐나')
elif menu=='3' or menu== '목욕하기' or menu== '목욕':
    print('으아!! 짜증!!')
else:
    print('없는 메뉴입니다.')
print()

#python 3.10버전에서 새로 도입된 문법 match-case [다른 언어에서 사용하는 switch-case문] 
# == 비교 연산을 가독성 좋게 해주는 문법
# match-case에서는 or 사용불가 --> | 를 사용한다. | 는 비트 연산자이지만, 논리연산과 같은 값이 나온다 오직 파이썬에서만.
match menu:
    case '1' | '밥먹기':
        print('굿')
    case '2' | '산책' | '산책하기':
        print('조아')  
    case '3' | '목욕' | '목욕하기':
        print('시러')
    case _:
        print('error')
print('-'*30,'\n')

#7) 특이한 키워드 pass -- 미완성 작업중일때.. 사용
a= 100
if a<100:
    print('aaa')
elif a<200:
    pass # 여기 작업을 다른 작업 후에 진행하고 싶을때.. 다른 작업할때 error나지않게 하기 위함.
elif a<300:
    pass
print('-'*30,'\n')

#8) 조건식을 쓸때 소괄호()를 생략해도 됨.
if (a<10):
    print('aaa')
elif a<100:
    print('aaaa')
print()

#9) one line if문, 조건의 실행문이 한줄이면.. 코드도 한줄로 써도 됨. (코드의 간결)
#1] if
age=25
if age>20:
    print('adult')          #원래 모습

if age>20: print('adult')   #one line if문

#2] if - else [순서: 실행문A - if() - else - 실행문B]
number= 10
if number%2==0:
    print('짝수')
else:
    print('홀수')       # 원래 모습

print('짝수') if number%2==0 else print('홀수') # one line if문

#3] if - elif - else
menu=1
print('Hello') if menu==1 else print('nice') if menu==2 else print('good')

#10) 삼항연산자 ? : [age>20 ? 'A' : 'B'] --다른 언어에 존재하는 삼항연산자를 one line if문으로 대응.
#ex) 사용자가 정수 2개를 입력하면.. 그 값중에 큰값이 max라는 변수에 저장되도록..
num1= 10
num2= 5

#num1과 num2중에서 큰값을 max변수에 대입
if num1>num2:
    max=num1
else:
    max= num2
print('둘 중에 큰 값은:',max)   # 원래 모습

# 삼항연산자 대응문법으로 처리
max= num1 if num1>num2 else num2 # one line if문

# ex) 학점 출력..을 삼항연산자(ternary operator)로..
score= 85
grade= 'A학점' if score>=90 else 'B학점' if score>=80 else 'C학점' if score>=70 else 'D학점' if score>=60 else 'F학점'
print('당신의 학점은:',grade)
print()

#10) 파이썬은 0과 같이 값이 없는 것을 제외하고는 모두 참으로 해석..

# 사용자가 입력해야하는데.. 안하고 그냥 엔터
text= input('글씨를 입력하세요: ')
# 사용자가 입력을 안했을 경우..를 대응하기 위해
if not text:
    print('입력해!!!!!!!!!!!!!!')
else:
    print('입력된 글씨는: ',text)
print('-'*30,'\n')

# 조건 사용할때 주의할 점.
aa='Hello'
n=5
if n<10:
    aa='nice'
print('aa:',aa)
print()

# if안에 넣어서 만든 변수는 조건 밖에서 쓸 수 없음. 굉장히 많이하는 실수
tt= None # 밖에 변수를 없는 값으로라도 만들어야 에러가 나지않음
n= 15

if n<10:
    tt='nice'
    print('안:',tt)
print('밖:',tt)





