# 1.
# 세 개의 정수를 인자로 전달받아서 그 중 가장 큰 수를 반환하는 함수와 가장 작은 수를 반환하는 함수를 정의해 보자.
# 그리고 이 함수를 호출하는 프로그램도 작성해보자. 
# [파이썬 내장함수 min, max를 직접 만들어 보아요. 함수의 이름은 각자 적절한 식별자를 명명하시오.]


def my_max(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)

my_max(-7,12,7)
print()

def my_min(d,e,f):
    if d<e and d<f:
        print(d)
    elif e<f:
        print(e)
    else:
        print(f)

my_min(3,7,-8)
print()

