# 네트워크상의 이미지 파일을 다운로드하는 프로그램

#requests [외부모듈 - 별도 설치필요 (터미널 > pip install requests)]

import requests
address= 'https://cdn.pixabay.com/photo/2016/11/29/13/49/christmas-background-1869989_1280.jpg' # 이미지 파일의 인터넷 경로(URL)
address= 'https://cdn.pixabay.com/photo/2017/11/05/08/38/christmas-2919725_1280.jpg'
address= input('다운로드할 이미지 URL 입력:')
response= requests.get(address)
print('응답코드:',response.status_code)
# print(response.text) # 이미지는 글씨가 아님. 고로 알수없는 글씨들이 표시됨
# 이미지는 2진수의 픽셀 정보를 가지고 있는 데이터 파일임
# response 응답객체는 본인이 읽어온 바이너리데이터를 16진수로 보여줄 수 있음
print(response.content)
print()

# 읽어온 이미지 파일데이터 덩어리를 내 컴퓨터에 파일로 저장하기(파일 처리 표준함수 open())
# file= open('download/aaa.jpg','wb') # wb: write binary

# 파일명이 고정값이면 기존 파일이 덮어쓰기되기에.. 중복되지 않는 파일명을 만들어야 함.
# 가장 많이 활용되는 방법은 날짜와 시간정보를 이용하여 파일명을 생성
import datetime
now= datetime.datetime.now()


# file_name= 'IMG_' + str(now)
# file_name= file_name.replace(' ','').replace('-','').replace(':','').replace('.','')
# file_name= file_name+'.png'

# 날짜를 이용한 특정 서식모양(format)으로 만들어주는 기능이 now 시간객체에 이미 존재함
# Y= yyyy, y= yy / M= minute, m= month ...
file_name= 'IMG_'+now.strftime('%Y%m%dd%H%M%S')+'.png'

print(file_name)

file= open('download/'+file_name,'wb')
file.write(response.content) # 바이너리 데이터를 파일에 쓰기!
file.close()

