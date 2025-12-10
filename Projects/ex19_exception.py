# 1. Error      (오류) : 문법적으로 문제가 있어서 처음부터 실행조차 불가능한 문제
# 2. Exception  (예외) : 실행 중(Run Time) 문제 발생 == Run Time Error

print('예외처리에 대해 알아봅니다.')
print()

#1) 에러인 경우.
# 10=a          # 에러는 오류난 해당줄만 실행이 안되는 게 아닌, 처음부터 실행불가
                # 해결방법은 문법에 맞게 코드를 수정..

#2) 예외인 상황.    
# print(10/0)     # 산수연산에서 0 나눗셈은 불가능한 연산.

# 예외가 발생하면 프로그램이 다운됨.. 아래에있는 정상적인 코드도 실행X
# [예외처리]라는 것은 예외가 발생하더라도 아래 코드들은 정상적으로(프로그램이 다운되지 않게) 실행되도록하는 문법

# 흔하게 볼 수 있는 예외 상황들
#1. 0 나눗셈
n=2
n=0
# 예외가 발생할 가능성이 있는 코드에 대해 예외처리 문법을 사용 [try - exception] 파이썬을 제외한 모든 언어는 (try - catch)이다.
try:
    print(10/n)
except: # 예외가 발생하면 실행되는 영역
    print(' 0 나눗셈은 불가능합니다.')

#2. 리스트의 인덱스번호를 잘못 사용하는 경우
aaa= [10,20,30]
try:
    print(aaa[3]) # 인덱스 번호 문제 발생
except:
    print('잘못된 인덱스 번호입니다.')

#3. 다른 자료형의 연산 [ 숫자+문자 ]
try:
    print(10+'5')
except:
    print('문자와 숫자는 연산이 불가능합니다.')

#4. 바꿀 수 없는 자료형으로 형변환 시도
try:
    print(10+int('3.14'))
except:
    print('정수모양의 문자열만 int로 변환할 수 있어요')

# 결국 예외처리라는 것은.. 예외가 발생되지 않도록 하는 것이 아니라
# 예외가 발생해도 프로그램이 다운되지 않도록 하는 기술
#------------------------------------------------------

#3) 코드의 가독성을 위해 등장한 else 영역 추가..
# 예외가 발생하지 않았을때 수행할 작업을 try 영역안에 모아서 쓰는 것이 가독성이 떨어져 등장한 문법

#ex) 정수 입력받아서 제곱하는 작업

# try 구문으로만 처리
# try:
#     #예외 발생 가능성이 있는 코드
#     number= int(input('정수 입력: '))
#     print(number**2)
# except:
#     print('정수만 입력 가능합니다.')

# # try 영역안에 모든 성공코드를 작성하지 않고..
# # 예외발생 가능성있는 코그만 try 영역에.. 예외가 아닐때(정상) 수행할 코드를 다른 영역에 작성하여 가독성 향상 - else

# try:
#     number= int(input('정수 입력: '))
# except:
#     print('정수만 입력 가능합니다.')
# else:
#     print(number**2)
#------------------------------------------------------
print()

#4) 예외발생 여부와 상관없이 무조건 수행할 작업이 있다면.. 사용하는 finally
#ex) 파일 읽기 작업중.. 예외발생.. 이로 인해.. close()의 미스
try:
    file= open('aaa.txt','r',encoding='utf-8')
    print(file.read())
    print(file.reah()) # 함수명을 잘못 입력하면 밑에 close를 건너뛰고 except로 넘어감
    file.close() # 무조건 실행해야되는 코드는 try영역에 작성X(실패시 실행을 안하기 때문에)
except:
    print('파일 읽기 작업중에 오류가')
finally:
    print('이 영역은 예외가 발생하든 안하든 무조건 실행되는 영역입니다.')
    file.close()

print('파일스트림이 닫혔나요?:',file.closed)
#------------------------------------------------------------
print()

#5) 예외가 발생했을때 그 이유를 알고싶다면..
try:
    print(10/0)
except Exception as e: #Exception 예외객체 사용 및 e라는 이름의 변수로 참조하여 제어
    print('error')
    print('에러종류: ',type(e))
    print('에러이유: ',e)
print()

try:
    aaa= [10,20,30]
    print[aaa[3]]
except Exception as e: #Exception 예외객체 사용 및 e라는 이름의 변수로 참조하여 제어
    print('error')
    print('에러종류: ',type(e))
    print('에러이유: ',e)
print()

# 이런식으로 에러의 종류를 알 수 있다면.. 에러별로 대응하는 코드가 가능함

#6) try영역안에 2개 이상의 에외가 발생할 가능성이 있는 경우도 존재함.
# try:
#     num1= int(input('입력: '))
#     num2= int(input('입력: '))

#     div= num1/num2
#     print('나눗셈 결과:',div)

# except ValueError as e:
#     print('숫자만 입력하세요',e)
# except ZeroDivisionError as e:
#     print('0나눗셈 불가능',e)
# except Exception as e:      # Exception 모든 종류의 에러
#     print('알 수 없는 에러 발생',e)     # 순차적으로 내려오기 때문에 마지막에 써야함.
print()
#------------------------------------------------------------
# [추가] 예외상황이 아닌데.. 개발자가 강제로 예외야!! 라고 문제를 발생시키는 문법 raise

#ex) 원래 파이썬은 계산의 결과가 음수라고 해서 예외는 아님..
# num= int(input('enter number: '))
# if num < 0:
#     raise Exception
# else:
#     print(num)
# print()

# 예외처리로 위 [음수값에 대한 예외](<원래 없는 예외, 내가 만든 예외)를 처리해보기
try:
    num= int(input('enter number: '))
    if num < 0:
        raise Exception
    else:
        print(num)
except:
    print('양수만 입력해!!!')
print()

# exception 발생 이후로 실행되지 않음 (이전까진 실행됨)
print()
print('-'*30,'\n')
print('프로그램 종료')
print()