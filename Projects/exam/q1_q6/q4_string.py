# 문자열 다루기 (기능 함수) 과제

# 1.
print("입력한 글자의 길이를 알 수 있는 프로그램입니다.")
print()

q1_massage= input('글을 입력하세요: ')

print('문자열의 길이:', len(q1_massage))
print('첫번째 문자:',q1_massage[0])
print('마지막 문자:',q1_massage[-1])
print('-'*30,'\n')

# 2.
# 아래와 같은 문자열 변수를 소문자로 바꾸고, 양쪽 공백을 제거하는 코드를 작성
print('문자가 공백없이 소문자로 나오면 성공입니다.')
print()
whitespace_strisng= "     PYTHON     "

print(whitespace_strisng.strip().lower())
print('-'*30,'\n')

# 3.
print('great가 문자열 안에 포함되어 있나요?')
print()

q3_string= 'Python is a great language'
print('great' in q3_string)
print('-'*30,'\n')

# 4.
print('전화 번호를 입력하세요')
print()
q4_input1= input('앞 번호를 입력하세요: ')
q4_input2= input('중간 번호를 입력하세요: ')
q4_input3= input('마지막 번호를 입력하세요: ')

print('입력된 전화번호는 [{}-{}-{}]입니다.'.format(q4_input1,q4_input2,q4_input3))
print('-'*30,'\n')

# 5.
print('이메일 주소에서 아이디와 메일 서버를 분리하여 출력합니다.')
print()

q5_input= (input('이메일 주소 입력(@포함): '))
q5_split= q5_input.split('@')

print('ID: ',q5_split[0])
print('사이트: ',q5_split[1])
print('-'*30,'\n')

# 6.
q6_massage='''
올해 신년 기자회견에서 저는 AI 연구와 AI 산업이 국가 경쟁력을 좌우할 것이라고 
말씀드립니다. 
정부는 공공 서비스에 ai를 적극 도입해 행정 효율성을 높일 계획입니다. 
특히 의료AI 분야와 재난 대응 AI 시스템은 국민 안전을 지키는 데 중요한 역할을 할 
것입니다. 
교육 영역에서는 ai 기반 맞춤형 학습과 AI 튜터링 서비스를 확대하겠습니다. 
중소기업의 생산성을 높이기 위해 AI 자동화와 AI 데이터 분석 지원 사업을 강화합니다. 
산업 전반의 데이터·AI 생태계를 정비해 혁신 기반을 구축하겠습니다. 
국방 분야에서도 ai 기술을 활용해 보다 정교한 위협 대응 체계를 마련하겠습니다. 
또한 교통·에너지 관리에 AI 예측 모델을 적용해 효율성을 높이겠습니다. 
정부는 AI 윤리 기준과 AI 안전 규범을 마련해 기술 발전이 책임 있게 이루어지도록 
하겠습니다. 
끝으로, ai 혁신이 모두에게 혜택이 될 수 있도록 포용적 성장을 이루겠습니다.
'''

print('앞뒤 공백을 제외한 총 글자수: ',len(q6_massage.strip()))
print('단어 사이 공백, 줄바꿈 문자도 제외한 글자수: ',len(q6_massage.replace(' ','').replace('\n','')))

q6_count=q6_massage.lower().count('ai')

print(f'AI가 총 {q6_count}번 언급되었습니다.')
print('-'*30,'\n')

