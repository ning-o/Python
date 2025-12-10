# 박스오피스 분석 프로그램
from datetime import datetime,timedelta
now= datetime.now()
# now= now- datetime.timedelta(days=1)  # 어제 날짜 구하기
# yesterday= now.strftime('%Y%m%d')

day_to_sunday= (now.weekday()+1)%7 # 오늘이 일요일이며녀 0일 차이
last_sunday = now- timedelta(days=day_to_sunday)

last_sunday= last_sunday.strftime('%Y%m%d')

import requests
address= 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=4341c5dd02e8c593d603234ce547b273&multiMovieYn=N&itemPerPage=5&weekGb=0&targetDt='+last_sunday
# multiMovieYn= "Y"(다양성 영화) or "N"(상업 영화) (default : 전체)
# Daily -> Weekly // boxO[daily -> weekly]
# itemPerPage= row 개수 지정 (default : “10”, 최대 : “10”)
# weekGb= “0” : 주간 (월~일), “1” : 주말 (금~일) (default), “2” : 주중 (월~목)
# repNationCd= “K: : 한국영화 “F” : 외국영화 (default : 전체)
reponse= requests.get(address)

boxO= reponse.json()
print()
print('-'*15)
print(boxO['boxOfficeResult']['boxofficeType'])
print('-'*15)

items= boxO['boxOfficeResult']['weeklyBoxOfficeList']

for item in items:
    rank= item['rank']
    name= item['movieNm']
    open_d= item['openDt']
    audiAcc= int(item['audiAcc'])
    salesAcc= int(item['salesAcc'])

    print('순위:',rank)
    print('제목:',name)
    print('개봉일:',open_d)
    print(f'관객수: {audiAcc:,} 명')
    print(f'누적 매출액: {salesAcc:,} 원')
    print('-'*20)
