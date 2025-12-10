import requests
import datetime

today= datetime.datetime.now().strftime('%Y%m%d')

url= f'https://apihub.kma.go.kr/api/typ01/url/sts_ta.php?tm1={today}&tm2={today}&lat=36.5&lon=126.5&help=0&disp=1&authKey=6U0VRntET2uNFUZ7RM9rww'

headers= {
    'User-Agent': 'Mozilla/5.0'
}


response= requests.get(url, headers=headers)

print('요청날짜:',today)
print(response.text[:500])


