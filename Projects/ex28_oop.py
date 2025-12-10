# OOP ( Object Oriented Programming ) - 객체 지향 프로그래밍
# 객체 지향을 위한 중요한 용어 : class(클래스), object(객체)

# class와 objecct의 필요성

# ex) 학생 성적을 분석하고 관리하는 서비스 개발

# 학생의 [이름, 국어, 영어, 수학, 평균] 데이터 저장


# 값을 저장해야하니 변수 필요
name= 'sam'
kor= 80
eng= 70
math= 90
aver= (kor+eng+math) / 3

# 학생 1의 값들을 출력
print(name, kor, eng, math, aver)
print()

# 두번째 학생이 있다면?
name2= 'robin'
kor2= 50
eng2= 40
math2= 60
aver2= (kor2+eng2+math2) / 3
print(name2, kor2, eng2, math2, aver2)
print()

# 이런 학생들이 10명.. 100명이면.. 
# 변수 하나에 연관있는 값(학생 한명의 데이터들..이름,국,영,수,평균)을 묶어서 저장하여 관리에 용이함
# 데이터를 묶어서 저장해주는 타입 [리스트], (튜플), {딕셔너리}을 이용

aaa= ['sam',70,80,90,80.0]
bbb= ['robin',40,50,60,50.0]
print(aaa)
print(bbb)
print()

# 학생의 성적 분서거을 위해 두명의 학생 성적 중 '국어' 성적만 뽑아서 출력해보기
print('학생 1의 국어성적:',aaa[1])
print('학생 2의 국어성적:',bbb[1])
print()
# 데이터 추출이 가능은 하지만.. 인덱스 번호라서 식별이 불편함

# key:value 쌍으로 데이터를 저장하는 dictionary 사용해보기
ccc= {'name':'sam','kor':70,'eng':80,'math':90}
ccc['aver']= (ccc['kor']+ccc['eng']+ccc['math'])/3
print(ccc)
print('학생 수학:',ccc['math']) # 식별자를 이용하기에 가독성이 좋음
print()

# ddd= {'name':'robin','kor':40,'eng':50...} # 식별자를 계속 쓰는 게 비효율
print('-'*30,'\n')

# [이름,국어,영어,수학,평균]을 한번에 저장할 수 있는 변수가 있다면..

# 똑같은 모양의 변수들을 dict처럼 묶어서 필요할때마다 개발자가 설계하여 사용할 수 있도록 제공되는 문법
# 이를 class(묶음 설계도)와 object(설계도로 만든 제품, 객체)라고 함

# class  : 연관있는 데이터(변수)와 기능(함수)을 묶어놓은 설계도
# object : class설계도를 기반으로 실제 메모리에 만들어진 제품

# 학생의 [이름, 국어, 영어, 수학, 평균] 변수를 하나의 그룹(class)으로 묶는다고 설계해보기.. 파이썬에게 이렇게 묶을 거라고 알려주는 설계도
# class 명명 규칙 : 기본적으로 변수 식별자 규칙과 유사함 // 표기법은 파스칼 표기법 권장(첫글자 대문자)
class Student:
    # 변수도 초기화가 필요하듯이 class묶음도 초기화 과정이 필요함
    # 이 class로 객체를 만들때 자동으로 처음 실행되는 특별한 영역(함수)이 존재함(생성자 함수)
    def __init__(self):
        print('Student 설계도(class)로 객체가 생성되었습니다.')

        # 이 제품이 가지고 있을 값들을 저장할 변수들을 선언
        # 변수명을 클래스 영역안에서 본인 것이라고 인식하는 키워드가 존재함. 그게 함수의 파라미터로 전달된 self
        # 이 클ㄹ래스의 소속임을 표현하는 self로 만들어진 변수를 [멤버변수]라고 부름
        self.name= 'sam'
        self.kor= 0
        self.eng= 0
        self.math= 0
        self.aver= (self.kor+self.eng+self.math)/3
    
    # 멤버변수의 값들을 알아서 출력해주는 기능함수를 정의 -- 멤버함수라고 부름(다른 용어로 '메소드'라고도 부름)
    def show(self): # 파이썬의 클래스 영역안에서 멤버변수를 지칭하려면 반드시 self. 와 함께.. 무조건 함수의 파라미터에 self가 전달되어야 함
        print('이름:',self.name)
        print('국어:',self.kor)
        print('영어:',self.eng)
        print('수학:',self.math)
        print('평균:',self.aver)
        print()

    # 멤버변수에 값을 대입해주는 기능함수 - 대입할 값을 함수의 파라미터로 받아서 멤버변수에 대입
    def set_members(self, name, kor, eng, math):
        self.name= name
        self.kor= kor
        self.gng= eng
        self.math= math
        self.aver= (kor+eng+math) / 3
    

    

# class는 설계도임. 아직 제품이 아니기에.. 클래스를 설계했다고해서 그 안에 코드가 실행되지 않아요 like 함수

# Student라는 이름을 가진 클래스(설계도)를 기반으로 제품(객체)을 만들어보기
# 객체 생성 문법 (함수 호출문과 유사함) : 클래스명()

Student() # 객체가 생성되면 __init__()함수의 영역이 실행됨.. 이때 이 제품안에 5개의 변수가 만들어짐

# 같은 설계도를 또 다른 제품(객체)을 생성할 수 있음.. 이때 이 제품안에 5개의 변수가 만들어짐
Student()

# 객체(5개의 변수를 한번에 가지고 있는 녀석)를 만들었으면 사용해야 하는데.. 
# 이 객체를 제어하는 변수가 없으면.. 사용불가
# 마치 리스트를 만들고 변수에 대입을 안한 거와 같은 상황
# [10,20,30]
# print('이름:', ???)

# 객체를 사용하려면 변수에 대입
stu1= Student() # stu1 이라는 변수를 이용하여 Student 설계도로 만든 객체를 제어할 수 있음.
print(stu1) # stu1이랄는 참조변수가 참조하고 있는 실제 Student객체의 위치(메모리 주소)를 출력함.
# stu1이 참조하는 Student객체 안에 있는 변수들을 사용하기[이때 사용하는 것이 . 연산자]
print('이름:',stu1.name)
print('국어:',stu1.kor)
print('영어:',stu1.eng)
print('수학:',stu1.math)
print()

# 객체 안에 있는 작은변수(멤버변수)들에 값들을 대입할때 리스트처럼 한번에 넣는 것은 불가능
stu1.kor= 70
stu1.eng= 80
stu1.math= 90
stu1.aver= (stu1.kor+stu1.eng+stu1.math)/3

print('이름:',stu1.name)
print('국어:',stu1.kor)
print('영어:',stu1.eng)
print('수학:',stu1.math)
print('평균:',stu1.aver)
print()

# 두번째 학생의 데이터 저장이 필요하면 변수 5개를 만들어야 하지만.. Stuudent라는 큰 덩어리를 설계해 놓았으니..
# Student 덩어리 객체를 하나 만들면 안에 멤버로... 5개의 변수가 한번에 만들어짐
stu2= Student()
stu2.name= 'robin'
stu2.kor= 40
stu2.eng= 50
stu2.math= 60
stu2.aver= (stu2.kor+stu2.eng+stu2.math)/3

# 멤버변수의 값 출력

print('이름:',stu2.name)
print('국어:',stu2.kor)
print('영어:',stu2.eng)
print('수학:',stu2.math)
print('평균:',stu2.aver)
print()

# 이런식이면.. 새로운 학생 만들고 출력때마다 출력코드를 매번 작성하는 것이 매우 번거로움
# 이 객체에게 본인의 멤버변수값들을 출력해주는 기능이 있다면.. 더 편하지 않을까
# 그래서 파이썬의 클래스 영역안에 변수 외에 함수도 미리 만들어 놓을 수 있음 .show()

# 세번째 학생
stu3= Student()
stu3.name= 'hong'
stu3.kor= 70
stu3.eng= 75
stu3.math= 80
stu3.aver= (stu3.kor+stu3.eng+stu3.math)/3

# 멤버값 출력할때 stu3객체가 가진 출력 기능함수를 호출
stu3.show()

# 객체를 만들고 그 멤버 변수에 값을 대입할때 하나씩 대입하는 것도 번거로움
# 전달할 값을 한번에 넣어주는 기능이 있다면.. 더 편하지 않을까
# Student 클래스를 설계할때 입력기능도 같이 설계..
stu4= Student()
stu4.set_members('kim', 50, 60, 70)
stu4.show()

stu5= Student()
stu5.set_members('lee', 10, 20, 30)
stu5.show()

stu6= Student()
stu6.set_members('park', 100, 90, 80)
stu6.show()

# 객체를 생성하고 언제나 값을 대입하는 기능을 호출함
# 객체를 생성할때 값을 전달해도 되지 않을까.. 객체가 생성될때 자동으로 호출되는 특별한 함수가 있음
# 이 특별한 함수를 '생성자 constructor 함수'라고 부름.. 파이썬은 이 용도의 함수명을 미리 정해놓음. __init__
# 이 생성자 함수의 파라미터 값을 전달하여.. 생성하면서 값 대입이 가능해짐

print('-'*30,'\n')
# 새로운 클래스를 설계하여.. 생성자 함수에 값 전달하는 실습 진행
# [이름, 나이, 주소] 정보를 그룹으로 묶어서 가질 수 있는 객체를 만들기 위한 클래스 설계
class Member:
    def __init__(self, name, age, address):
        # [이름, 나이, 주소]를 저장하기 위한 멤버변수 선언, 멤버변수는 이 클래스의 소속임을 보여주기 위해 self키워드 필요
        self.name= name
        self.age= age
        self.address= address

    # 멤버변수를 출력해주는 기능함수 정의 - 클래스 안에 함수들은 무조건 첫번째 파라미터로 self를 등록
    def show(self):
        print('이름:',self.name)
        print('나이:',self.age)
        print('주소:',self.address)
        print()

# 위 설계도 class로 [이름,나이,주소]를 한번에 저장하는 객체 생성
m1= Member('sam',20,'seoul')
m2= Member('robin',25,'incheon')
m3= Member('hong',30,'paris')

m1.show()
m2.show()
m3.show()

# 각 객체들의 나이만 출력하려면..
print('나이:',m1.age)
print('나이:',m2.age)
print('나이:',m3.age)

member_list= [m1, m2, m3, Member('hong',40,'new york')]
for member in member_list:
    member.show()

print()
#------------------------------------------------------------------------

# 여러 학생의 [이름, 파이썬, 웹, AI] 성적 데이터를 저장하기 편하도록 4개 데이터를 한번에 저장하는 객체를 설계하여 사용
class Stu:
    #객체의 초기값을 설정하기 위해 생성자 함수 -- 객체 생성할때 전달되는 4개의 값으로 초기화
    def __init__(self, name, python, web, ai):
        self.name= name
        self.python= python
        self.web= web
        self.ai= ai

    # 멤버변수의 값을 출력해주는 기능함수 설계하기 - 멤버함수의 첫번째 파라미터에 언제나 self를 등록
    def show(self):
        print(self.name, self.python, self.web, self.ai)
        print()
    
    # 총점을 계산하여 리턴 해주는 기능 함수 설계하기
    def get_total(self):
        return self.python+self.web+self.ai


# class는 단지 설계도임. 아직.. 객체가 실행되지 않았기에 사용이 불가능
# class 설계대로 멤버(변수 4개, 함수 1개)를 가지는 객체를 생성하여 사용
s1= Stu('sam', 80, 70, 50)
s1.show()

s2= Stu('robin', 60, 40, 20)
s2.show()

# 만약 학생별 성적의 총점을 저장하고 싶다면?
total1= s1.get_total()
print('1번 학생의 총점:',total1)

total2= s2.get_total()
print('2번 학생의 총점:',total2)
print()

# module_a에 Person 클래스를 설계하고 사용해보기

from module_a import Person
p1= Person('park', 20)
p1.display()

p2= Person('choi', 30)
p2.display()

print()
print('마지막 코드..')
print()

# 객체안에 변수와 함수가 같이 존재함..
# 파이썬은 객체밖에도 변수와 함수를 만들어 사용할 수 있음

# 그래서 용어를 분리하여 부름
# 객체 밖에서 값을 저장하는 것을 '변수 varidable', 기능 코드가 있는 영역을 '함수 function'
# 객체 안에서 값을 저장하는 것을 '속성 propterty'(멤버변수), 기능 코드가 있는 영역을 '메소드 method'(멤버함수) // 괄호 안에 있는 건 타언어에서 공통적으로 지칭하는 언어

a=10 #변수
def aaa(): #함수
    pass
p1.name  #객체의 속성값
p1.display() #객체의 메소드

