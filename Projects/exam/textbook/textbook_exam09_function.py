#-------------p.278

def print_n_times(n,*values):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        print()
print_n_times(3,'안녕','반갑','슴다?')

# 범위 내부의 정수를 모두 더하는 함수 --p.287
def sum_all(start,end):
    output=0
    for i in range(start,end+1):
        output += i
    return output

print('0 to 100:', sum_all(0,100))
print('0 to 100:', sum_all(0,1000))
print('0 to 100:', sum_all(50,100))
print('0 to 100:', sum_all(50,1000))
print()

def sum_all(start=0, end=100, step=1):
    output=0
    for i in range(start, end+1, step):
        output += i
    return output

print('A.',sum_all(0,100,10))
print('B.',sum_all(end=100))
print('C.',sum_all(end=100, step=2))
print()

# 도전문제 -----p.291
# 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 만들어보세요

def mul(*values):
    result= 1
    for i in values:
        result *=i
    print(result)
mul(5,7,9,10)
