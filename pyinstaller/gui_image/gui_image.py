# pyinstaller 모듈을 이용하여 실행파일을 만들면 기존에 사용하던 상대경로가 맞지 않게됨
# 파이썬만의 특정 폴더 영역으로 리소스(코드를 제외한 나머지 파일들 이미지, 영상, 폰트 등등)를 위치한 후 실행함
# 그래서 코드에서.. 이 경로를 기반으로 리소스의 경로를 지정해야 함.

# pyinstaller -w -F --add-data resources;리소스폴더명 파일명      ----리소스 있는 프로그램
# pyinstaller -w -F 파일명                                      ----리소스 없는 프로그램

import sys
import os

# 상대경로를 파라미터로 받아서 리소스용 경로를 만들어주는 기능함수를 미리 정의
def resourse_path(path):

    try:
        base_path= sys._MEIPASS
    except:
        base_path= os.path.abspath('./')

    #2개의 경로를 합성해주는 기능
    return os.path.join(base_path, path)


from tkinter import *

window= Tk()

img= PhotoImage(file=resourse_path('resources/image/ms19.png')) # ./ (같은폴더) 는 안써도 상관없음
label= Label(window, image=img)
label.pack()

window.mainloop()
