# 외부모듈 - 파이썬팀이 아닌 개인 또는 회사에서 별도로 개발한 파이썬 코드들의 집합체(모듈)

# 파이썬팀에서 개발한 모듈이 아니기에.. 파이썬 설치할때 같이 설치되어 있지 않음.
# 그래서 사용하려면.. 그 모듈을 다운로드하여 컴퓨터에 설치 후 import해서 사용해야 함.
# 외부모듈을 서버에 가지고 있으면서 필요할때 설치해주는 도구 pip (packing installer for python) - CLI 설치도구

#1. requests - 자동 디코딩, 자동 예외처리, json 모듈이 이미 연동되어 있음, http 요청 작업이 용이함, 쿠키, 세션, 파일업로드 등 많은 작업이 편하게 구현 가능
#설치방법) vscode에서 터미널(cmd, 명령프롬프트) 창을 열고 설치 명령어 입력
# > pip (or pip3) install 모듈명

# 설치완료되면 표준모듈처럼 import해서 사용
import requests

address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt'
response= requests.get(address) # 서버의 데이터를 요청한 결과정보를 가진 객체를 리턴
# 응답객체 response를 통해 데이터와 상태정보를 알 수 있음.
print('응답 코드 번호:',response.status_code)
print('읽어 들인 데이터:')
print(response.text)
print()

# json 모듈 기능도 이미 포함된 상태
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/hhh.json'
response= requests.get(address)
print(response.status_code)
print(response.text)
 
aa= response.json() # 알아서... json문자열을 분석하여 dictionary로..
print(aa['data_title'])
print(aa['total_count'])
print('-'*30,'\n')

# [간단하게 open api 실습]

# 조회날짜(어제)가 고정되면 안됨. 변수여야 함.
# 날짜 모듈을 이용하여 오늘의 날짜 얻어오기
import datetime

now= datetime.datetime.now() # 오늘
now= now- datetime.timedelta(days=1)
# 'yyyymmdd'형식 만들기
yesterday= str(now.year) + str(now.month) + str(now.day)
print(yesterday)
yesterday= "{:04d}{:02d}{:02d}".format(now.year,now.month,now.day)
print(yesterday)

# 제일 쉬운 방법-----------------------
yesterday= now.strftime('%Y%m%d')
print(yesterday)
#------------------------------------

yesterday= '20251130' #yyyymmdd

address= 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=4341c5dd02e8c593d603234ce547b273&targetDt='+yesterday
response= requests.get(address)
print(response.status_code)
print(response.text)
print()

aa= response.json()
print(aa["boxOfficeResult"]["boxofficeType"])
print()

items= aa["boxOfficeResult"]["weeklyBoxOfficeList"]
for item in items:
    rank= item['rank']
    movie_name= item["movieNm"]
    open_date= item['openDt']
    audience_acc= item['audiAcc']

    print('랭킹:',rank)
    print('제목:',movie_name)
    print('개봉일:',open_date)
    print('누적관객수:',audience_acc)
    print('-'*30)
print()

