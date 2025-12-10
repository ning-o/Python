# python desktop GUI 만들기

# 표준모듈인 tkinter 사용 [ Tk(툴킷) interface ]

from tkinter import * # tkinter 모듈안에 있는 모든 클래스,함수,변수 등을 import (하위 모듈{}은 불러오지 않음.)

# GUI 화면을 구성하는 구성요소들을 tkinter에서는 [위젯]이라고 부름
# 위젯 종류
#1. 컨테이너용 위젯 [다른 위젯들을 담기위한 위젯] : Tk, Frame ... 
#2. 단순 위젯 : Label, Button, Entry ....

# GUI 프로그램의 제작 프로세스 : 최상위 위젯을 만들고.. 그 안에 원하는 위젯들을 배치 관리자를 통해 배치..

#1] 최상위 윈도우 창 객체 생성
window= Tk()

# 화면 구성은 최상위 위젯의 mainloop() 요청 전에 추가 해야함. 그래서 2번보다 위에 코드를 써야함
#3] 위도우 창의 제목 설정
window.title('this is python gui') 

#4] 위도우 창 크기 + 위치 설정
window.geometry('400x500+100+100') # 너비x높이+x축+y축 [+왼쪽부터, +위쪽부터]
window.geometry('400x500-200+100') # 너비x높이+x축+y축 [-오른쪽부터, +위쪽부터]
window.geometry('400x500-200-100') # 너비x높이+x축+y축 [-오른쪽부터, -아래쪽부터]
window.geometry('400x500-400+100') # 맨밑에 값으로 적용

#5] 창 크기 조절을 막을 수 있음
window.resizable(False,True)    # False= 0, True= 1 로도 설정할 수 있음
window.resizable(height=False)  # 파라미터명을 쓰지 않으면 순서대로 입력, 순서 상관없이 값을 주고 싶으면 파라미터 명 입력
window.resizable(width=0, height=1) # 어떤값이 무엇인지 주석을 달아줘야하기 때문에 그냥 파라미터 이름을 쓰는 것도 좋은 방법

# GUI의 window창에는 print()로 출력 안됨. 글씨를 보여주는 위젯(구성요소)을 만들어서 그 안에 글씨를 쓰고 window에 배치
#6] Label
label= Label(window, text='Hello. Python GUI') # 이 위젯이 붙을 컨테이너 위젯을 지정 후 보여줄 글씨 지정
# 라벨을 적절한 위치에 배치해주는 기능 pack() : 추후 수업
label.pack()

# 글씨를 하나 더 보여주려면.. 또 다른 Label 위젯 필요
label2= Label(window, text='nice to meet you.', bg='yellow', fg='blue') # fg= 글씨색, bg= 글씨 배경색(pack 사이즈)
label2.pack()

# 사이즈를 지정해보기
label3= Label(window, text='안녕하세요', bg='black', fg='white', width=10, height=3) # 너비 10글자, 세로 3글자(알파벳 사이즈, 한글은 한글자에 2글자 사이즈)
label3.pack()

# 폰트 지정해보기
label4= Label(window, text='have a good day. 반가워요', font='times 20 bold italic') # font= 글꼴(폰트명), 크기, 볼드체, 이텔릭
label4.pack()

#7] 버튼 추가하기
def aaa():
    print('clicked!!!!')

btn= Button(window, text='눌러주세요', padx=10, pady=10, command=aaa) # 버튼의 패딩 x,y // command= 버튼 클릭시 실행될 함수의 이름만 ()빼고 
# 여기서 실행될 함수는 버튼보다 위에 정의 되어 있어야 함
btn.pack()

#8] 버튼 클릭할때 라벨이 보여주는 글씨 변경
label5=  Label(window, text='hello world')
label5.pack()

num= 0
def bbb():
    global num
    num= num+1
    label5.config(text='clicked button!!! : '+ str(num))

btn2= Button(window, text='change text', command=bbb)
btn2.pack()

#9] Entry 사용자로부터 한줄 텍스트를 입력받는 위젯
entry= Entry(window)
entry.pack()

#버튼 클릭할때.. Entry에 써있는 글씨를 Label에 보여주기
def ccc():
    value= entry.get()
    label6.config(text=value)

btn3= Button(window, text='입력 완료', command=ccc)
btn3.pack()

label6= Label(window, text='')
label6.pack()

# 10] 여러줄 입력이 가능한 위젯
text= Text(window, width=30, height=3) #30칸, 3줄
text.pack()

# 11] 버튼 클릭할때 경고(알림)창 보이기
from tkinter import messagebox # 하위모듈 import

def ddd():
    value= text.get('1.0', END) # '1.0' 첫번째 줄(1)의 첫번째 칸(0)에서 부터 END(끝)까지 값을 읽어와라
    messagebox.showinfo('메시지 값',value) # 알림창의 타이틀, 메시지

btn4= Button(window, text='메시지 읽기', command=ddd)
btn4.pack()



#2] # 최상위 윈도우가 화면에 보여지며.. 사용자의 마우스 이동, 클릭, 버튼 클릭 같은 이벤트처리를 지속적으로 수행하도록 요청하면 화면에 윈도우가 보임
window.mainloop()


