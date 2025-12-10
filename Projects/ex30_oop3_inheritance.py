# 상속 inheritance -- 이미 설계된 다른 class를 상속받아 새로운 멤버만 추가하는 문법

# 문법 학습전에 대략적인.. 상속의 필요성[개념]을 보여주는 예
# ex) 게임 개발.. 로봇 캐릭터 여러개 필요 (이동기능, 공격기능)
class Robot:
    #이동 기능
    def move(self):
        print('아장 아장...')
    #공격 기능
    def attack(self):
        print('주먹 발사!!')

#Robot 객체 생서어
r= Robot()
r.move()
r.attack()
print()

r2= Robot()
r2.move()
r2.attack()
print()

# 캐릭터 종류를 추가.. [공중유닛]
# FlyRobot 설계 ( Robot 기능 + 날수있는 기능 )
# 원래 있던 Robot 클래스에 추가하면 모든 로봇이 같은 기능이 생기기 때문에 별도의 설계 도면이 필요
class FlyRobot:
    #이동 기능
    def move(self):
        print('아장 아장...')
    #공격 기능
    def attack(self):
        print('주먹 발사!!')
    #날아다니는 기능(new)
    def fly(self):
        print('날아서 이동~~')

fr= FlyRobot()
fr.move()
fr.attack()
fr.fly()
print()

# 캐릭터 종류를 추가.. [해상유닛] -- ( Robot 기능 + 수영 기능 )
class SwimmingRobot(Robot): # Robot 클래스의 기능들을 굳이 직접 다시 작성하지 않고 그대로 가져오기(상속 inheritance)\
    # 이미 Robot의 기능을 보유한 상태
    # 새로운 기능만 추가하면 됨
    def swimming(self):
        print('음~파 음~파')

sr= SwimmingRobot()
sr.move()   # 만든적 없는 메소드.. Robot클래스에 있던 메소드를 상속받아 사용
sr.attack()
sr.swimming()
print('-'*30,'\n')

# 상속 문법 조금 더 알아보기
# First - Secoond

class First:
    #생성자를 만들어서 멤버변수 a만들기
    def __init__(self):
        self.a= 10
        print('First 객체가 생성되었습니다.')

    #멤버변수를 출력 기능 메소드
    def show(self):
        print('a:', self.a)
    
# First 클래스를 상속하는 Second 클래스 설계
class Second(First):
    # 아무것도 안해도 이미 First의 멤버들[a, show()]를 보유한 상태
    
    # Second 클래스도 본인의 멤버변수를 만들기 위해 초기화 영역(생성자 함수)추가
    # must [super() 이 상속해준 클래스 객체를 의미함]
    def __init__(self):
        super().__init__() # 명시적으로 상속해준 클래스의 생성자 함수를 호출해야만 함
        self.b= 20
        print('Second 객체를 생성했습니다.')

    #멤버값 출력기능 만들기.. [기존에 있는 show()기능을 다시 만들기 override]
    def show(self):
        # 상속해준 멤버 a의 출력은 그 클래스의 기능으로 출력하는 것을 권장
        super().show() # First의 show()가 발동
        print('b:', self.b)



# Second 객체 생성
s= Second() # 상속해준 First 객체도 같이 생성됨
# 상속해준 Fisrst의 멤버를 사용
print(s.a) # 상속문법의 진정한 의미는.. 상속해준 First 객체의 멤버를 마치 내것처럼 사용할 수 있도록 해주는 문법
print(s.b) # Second에서 새로만든 변수
# 멤버값을 출력하는 기능을 사용해보기
# s.show() # 상속받은 멤버 출력기능을 내것처럼 호출해보기 [새로 추가된 Second의 b변수를 출력하지 않음]
# show() 기능을 오버라이드 하여.. 개선된 기능 사용
s.show()
print()

print('-'*30,'\n')

# 상속과 오버라이드 메소드 사용에 대한 마지막 연습 예제
# ex) 어떤 대학 웹사이트의 회원데이터 저장 [회원종류 여러개..]

# 일반회원 : 이름, 나이
# 학   생 : 이름, 나이, 전공
# 교   수 : 이름, 나이, 연구과제
# 근로학생 : 이름, 나이, 전공, 업무

# 일반회원 데이터를 저장하기 위한 클래스 설계
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        print('Person 객체 생성')

    def show(self):
        print('이름:', self.name)
        print('나이:', self.age)
        
p= Person('sam', 20)
p.show()
print()

# 학생 회원 [ 일반회원+전공 ]
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major= major
        print('Student 객체 생성')
    
    def show(self):
        super().show()
        print('전공:', self.major)

s= Student ('robin', 23, 'ai web')
s.show()
print()

# 교수 회원 [ 일반회원+연구과제 ]
class Professor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject= subject
        print('Professor 객체 생성')
    
    def show(self):
        super().show()
        print('연구과제:',self.subject)

pro= Professor('park', 45, 'ai data analysis')
pro.show()
print()

# 근로 학생 [ 학생회원+업무 ]
class WorkStudent(Student):
    def __init__(self, name, age, major, task):
        super().__init__(name, age, major)
        self.task= task
        print('WorkStudent 객체 생성')
    
    def show(self):
        super().show()
        print('업무:', self.task)

ws= WorkStudent('hong', 25, 'data', 'pc management')
ws.show()

