# 화면출력 : print() 과제

# 1.
print("# 1.")
print("홍길동")
print("홍 길 동")
print("홍  길  동")
print("-"*30,'\n')

# 2. print() 기능을 한번만 사용하여 문제 1과 같은 결과 출력
print("# 2.")
print("홍길동\n홍 길 동\n홍  길  동")
print()

# 3. [이름,나이,주소]를 print()로 출력하기.
print("# 3.")
print("""제 이름은 홍길동 입니다.
제 나이는 20살이고요.
제가 사는 곳은 seoul입니다.""")
print("-"*30,'\n')

# 4. 
# 1) #3의 출력을 .format() 포멧 기능을 사용하여 출력하기.
print("# 4.")
print("제 이름은 {}입니다.\n제 나이는 {}살 이고요.\n제가 사는 곳은 {}입니다.".format("홍길동",20,"seoul"))
print("-"*30)
# 1) #3의 출력을 f"" 포멧 기능을 사용하여 출력하기.
print(f"제 이름은 {"홍길동"}입니다.\n제 나이는 {20}살 이고요.\n 제가 사는 곳은 {"seoul"}입니다.")
print("-"*30,'\n')

# 5.
print(4,'+',5,'=',4+5)
print(7,'x',9,'=',7*9)
print("-"*30,'\n')

# 6. 5 문제의 방식을 이용해서 구구단 5단을 출력해보자
print(f"{5} x {1} = {5*1}")
print(f"{5} x {2} = {5*2}")
print(f"{5} x {3} = {5*3}")
print(f"{5} x {4} = {5*4}")
print(f"{5} x {5} = {5*5}")
print(f"{5} x {6} = {5*6}")
print(f"{5} x {7} = {5*7}")
print(f"{5} x {8} = {5*8}")
print(f"{5} x {9} = {5*9}")
print("-"*30,'\n')

# 7.
print("{} x {} = {}".format( 5 , 1 , 5*1 ))
print("{} x {} = {}".format( 5 , 2 , 5*2 ))
print("{} x {} = {}".format( 5 , 3 , 5*3 ))
print("{} x {} = {}".format( 5 , 4 , 5*4 ))
print("{} x {} = {}".format( 5 , 5 , 5*5 ))
print("{} x {} = {}".format( 5 , 6 , 5*6 ))
print("{} x {} = {}".format( 5 , 7 , 5*7 ))
print("{} x {} = {}".format( 5 , 8 , 5*8 ))
print("{} x {} = {}".format( 5 , 9 , 5*9 ))
print("-"*30,'\n')

# 8.
print('   *')
print('  ***')
print(' *****')
print('*******')
print()

# 9.

print('-'*40)
print("번호",'\t',"이름",'\t',"나이",'\t',"전공",'\t',"주소")
print('-'*40)
print("1",'\t',"sam",'\t',"20",'\t',"web",'\t',"seoul")
print(f"{2}\t{"robin"}\t{25}\t{"ai"}\t{"busan"}")
print(f"{3}\t{"park"}\t{30}\t{"data"}\t{"incheon"}")
print()

# 10. print()는 한번만 사용하여 여러줄 문자열 출력하기

print("""파이썬은
웹 애플리케이션, 데이터 과학, 인공지능 등
다양한 분야에 사용되는 배우기 쉽고 효율적인
프로그래밍 언어입니다.""")
print()



# 예습 : input()

print("입력한 수의 곱한 값이 출력됩니다.")

a1 = input("정수 입력: ")
a = int(a1)

b1 = input("정수 입력: ")
b = int(b1)

print(a,'x',b,'=',a*b)
