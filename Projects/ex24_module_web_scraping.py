# 웹 스크래핑 : 웹 페이지에서 특정 정보를 추출하는 작업

# 외부 모듈 : requests, beautifulsoup4 [별도 설치 필요]

# 웹 페이지를 분석 - 웹 페이지를 만드는 문법 HTML, CSS, JavaScript

# 아주 간단한 웹페이지 만들어보기. [HTML, CSS, JavaScript 언어를 다뤄보기. (web-test)]

import requests
reponse= requests.get('https://2017mrhi.github.io/web-test/index.html')
print(reponse.text)
print()

# html 웹문서를 분석.. 요소들을 찾아서 안에 있는 값을 뽑아내기 [외부모듈 BeautifulSoup]
from bs4 import BeautifulSoup

# HTML분석가 객체를 생성
soup= BeautifulSoup(reponse.text, 'html.parser')

# p 요소들 모두 찾아보기
p_list= soup.select('p')    # 리스트로 찾아오기
print(len(p_list))

print(p_list[0].string)
print(p_list[1].string)

# 아이디로 찾기 - 이미지 경로 찾기
img= soup.select_one('#kk') # 하나만 찾아오기
print('이미지 경로:',img.get('src'))  # src 속성의 값을 얻어오기

# 클래스로 찾기
es= soup.select('.aa')
print(es[1].string)
print()
#-------------------------------------------------------------------------------

#[실습] 네이버 금융 페이지의 '코스피 지수' 스크래핑 해보기 (주의. 막 실행하면 안됨)
import requests
from bs4 import BeautifulSoup

response= requests.get('https://finance.naver.com/sise/')
# print(response.text)
soup= BeautifulSoup(response.text,'html.parser')

# 웹 문서에서 특정 요소를 찾기
span_element= soup.select_one('#KOSPI_now')
print('코스피 지수:',span_element.string)

