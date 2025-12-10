# 프로그램에서 사용하는 대부분의 데이터는 문자열인 경우가 많음.
# 문자열의 연산자와 기능함수 알아보기..

# 문자열 연산자 3개

# 1. + 결합연산자
print('aaa'+'bbb')
# 2. * 반복연산자
print('nice'*5)
# [] 인덱싱/슬라이싱 연산자
s= "Hello world"
print(s[2])     # 2번 인덱스 위치의 문자 1개를 출력 [인덱싱]
print(s[2:8])   # 2~8번 전까지 (2~7) [슬라이싱]
print(s[2:])    # 2번부터~ 끝까지
print(s[:5])    # 처음부터~ 4까지
print(s[-2])    # 뒤에서 2번 위치
print()

# 문자열의 길이(length)[글자수]를 알려주는 파이썬의 내장함수
a= len(s)
print('글자수: ',a)
print()

# 문자열 데이터가 가진 유용한 기능 함수들 알아보기.
#1) "".format() -- 특정한 서식모양으로 문자열을 만들어주는 기능

#2) upper() , lower() -- 대소문자 변환 가능
print('Hello'.upper())
print('Hello'.lower())

# 문자열을 변수에 대입하여 저장하면 변수명으로 기능 사용 가능
word= 'Machine Learning'
print(word.upper())
print(word.lower())
# [중요!] 기능을 사용하더라도 원본 문자열을 변경되지 않음.
print(word) 
s= word.upper()
print(s)
print()

#3) .strip() : 문자열의 양옆의 공백을 제거하는 기능함수
word= '    Hello    '
print(word)
print(word.strip()) #문자열 가운데 공백은 제거하지 않음
# 검색어 비교.. 또는 아이디 비교 작업할때 필수로 공백제거 후 비교함
print(word=='Hello')            # False
print(word.strip()=='Hello')    # True

#4) .find() : 특정 문자의 인덱스 번호 위치를 찾아주기.
s= 'Hello world. android. ios. ai. world'
print(s.find('world'))      # 찾은 글씨의 첫번째 글자 인덱스 번호
print(s.find('ANDTOID'))    # 대소문자는 다른 글자임. [못 찾으면 -1]
# 혹시 같은 문자가 여러개면.. 앞에서부터 검색하기에.. 앞에 번호 찾고 기능 멈춤
# 만약 뒤에 있는 문자도 찾으려면 추가 find()
idx= s.find('world') # 6
print(s.find('world', idx+1)) # 앞에 찾은 글씨 인덱스 번호 다음부터 다시 찾아라
print()

#5) in 연산자 [기능함수 아님.. ()없음] -- 특정문자가 그 문자열안에 있는지 여부(True/False)를 알려주는 연산자
print('world' in s) # s라는 변수가 가진 문자열안에 'world'라는 글씨가 있는지 확인
print('WORLD' in s) # 대소문자 구분이라 False
# 대소문자 구분없이 확인하고 싶다면.. upper() , lower() 활용
print('WORLD' in s.upper())

#6) replace - 글자 바꿔치기..
s= 'Hello world. nice world. good world'
# world 글씨들을 python이라는 글씨로 변경해서 출력.
print(s.replace('world','python'))
print(s) # 기능을 사용해도 원본은 불변
print(s.replace('WorLD','coding')) # 대소문자 구분 -> 바꿀 글씨가 없으면 원래 그대로 출력.
# 대소문자 구분없이 확인하고 싶다면.. upper() , lower() 활용
print(s.replace('WorLD'.lower(),'coding'))

# replace를 이용하면.. 글씨 사이의 공백문자(띄어쓰기) 제거 가능
s= s.replace(' ','') 
print(s)
s= s.replace('\n','') # 이렇게 만들면 갱신 가능
print(s)
# 비속어 걸러내기..
s= s.replace('FuXX','^^')
s= s.replace('개XX','^^')
s= s.replace('ㅈXX','^^')
s= s.replace('ㅁXX','^^')
print()

#7) .split() : 특정 문자를 기준으로 글씨를 나누어서 [리스트:여러 데이터를 한번에 가지는 변수]로 만들어주는 기능함수
csv= 'sam,20,seoul'
aaa= csv.split(',') # ,(콤마)를 기준으로 갈라줘
print(aaa)
print(aaa[0])
print()

#8) isXXX() 기능함수들..
#8.1] 알파벳으로만 이루어졌는가?
print('Hello'.isalpha())            # True
print('Hello123'.isalpha())         # False
print('Hello안녕하세요'.isalpha())    # True

#8.2] 숫자로만 이루어졌나요?
print('1234'.isnumeric())
print('1234abc'.isalnum())
# int() 형변환이 가능한지를 알 수 있음.
print('3.14'.isnumeric())           # False  .은 특수문자
print('300      '.isnumeric())      # F    공백은 특수문자
print('300      '.strip().isnumeric()) # T    strip()으로 공백을 날리고 --> isnumeric() 진행
# 로마 숫자도 허용
# 윗첨자 숫자도 허용
print('')

#8.3] 로마자는 제외한 숫자만 허용 [아라비아숫자+윗첨자]
print('1234'.isdigit())

#8.4] 오직 아라비아 숫자만 허용
print('1234'.isdecimal())

#8.5] 알파벳과 숫자로만 이루어졌는가? (특수문자 제외)
print('Hello123'.isalnum())         # T
print('Hello123!!'.isalnum())       # F
print('Hello     123'.isalnum())    # F

#8.6] 모두 소문자인가? (띄어쓰기는 신경쓰지 않음)
print('Hello world'.islower())
print('hello world'.islower())
print()

#9] count() : 문자열안에 특정 단어가 몇개인지 알려주는 기능함수
message= 'EDA(Exploratory Data Analysis) : 탐색적 데이터 분석. data를 다양한 각도에서 관찰하고 이해하는 첫번째 단계. 시각화와 통계적 기법을 사용하여 Data를 분석합니다.'
print('data 문자의 개수: ', message.count('data'))
print('data 문자의 개수: ', message.lower().count('data'))

# 위 9개 말고도.. 문자열에는 많은 기능함수들이 존재함.
# 나머지는 필요할 때 검색하여 사용하세요..
