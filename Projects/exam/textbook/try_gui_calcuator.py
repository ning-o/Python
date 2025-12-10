
from tkinter import *

window= Tk()
window.title('계산기')
window.resizable(False,False)
window.geometry('400x500-200+100')

# 맨위 결과창
frame1= Frame(window, padx=10, pady=10)
frame1.pack(fill='x')

listbox_result= Listbox(frame1, font=('',16), height=2)
listbox_result.pack(fill='x')

# 입력 수식 저장 변수
current_expr= ''

# 결과창 업데이트
def update_display():
    listbox_result.delete(0, END)
    listbox_result.insert(END, current_expr)

# 버튼 클릭 처리
def add_value(value):
    global current_expr
    #화면 표시용 -> 그대로
    # 실제 계산용-> x->*, ÷->/
    if value=='x':
        current_expr+='*'
    elif value=='÷':
        current_expr+='/'
    else:
        current_expr+=str(value)

    update_display()

# 전체 지우기
def clear():
    global current_expr
    current_expr=''
    update_display()

# 계산=
def calculate():
    global current_expr
    try:
        result= str(eval(current_expr))
        listbox_result.delete(0, END)
        listbox_result.insert(END, result)
        current_expr = result
    except:
        current_expr=''
        listbox_result.delete(0,END)
        listbox_result.insert(END, 'Error')

# 버튼 프레임
frame2= Frame(window, padx=10, pady=10, bg='tomato')
frame2.pack(fill='x')

# 계산기 버튼 배열
buttons=[
    [7,8,9,'x'],
    [4,5,6,'-'],
    [1,2,3,'+'],
    ['c',0,'.','÷'],
    ['=']
]
# 버튼 크기
btn_w, btn_h= 6, 3

# 버튼 생성
for r in range(len(buttons)):
    for c in range(len(buttons[r])):
        text= buttons[r][c]

        # 기능 연결
        if text=='c':
            cmd= clear
        elif text == '=':
            cmd= calculate
        else:
            cmd= lambda x=text: add_value(x)


        btn=Button(
            frame2,
            text= text,
            width=btn_w,
            height=btn_h,
            font=('',12,'bold'),
            command=cmd
        )
        # '=' 버튼만 마지막 줄 가운데로 배치
        if text == '=':
            btn.grid(row=r,column=0, columnspan=4, sticky='we', padx=5, pady=5)
        else:
            btn.grid(row=r, column=c, padx=5, pady=5)

window.mainloop()
