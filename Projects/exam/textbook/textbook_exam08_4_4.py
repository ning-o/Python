#-----p.252
#reversed()함수

list_a= [1,2,3,4,5]
list_reversed= reversed(list_a)

print("# reversed() 함수")
print("reversed[1,2,3,4,5]:", list_reversed)
print('List(reversed([1,2,3,4,5])):',list(list_reversed))
print()

print('#reversed() 함수와 반복문')
print('for i in reversed([1,2,3,4,5]):')
for i in reversed(list_a):
    print('-', i)
print()

#enumerate()함수와 리스트

example_list= ['요소A','요소B','요소C']
print('단순 출력')
print(example_list)
print()

print('# enumerate() 함수 적용 출력')
print(enumerate(example_list))
print()

print('# list() 함수로 강제 변환 출력')
print(list(enumerate(example_list)))
print()

print('반복문과 조합하기')
for i, value in enumerate(example_list):
    print('{}번째 요소는 {}입니다.'.format(i,value))
print()

#딕셔너리의 items() 함수와 반복문
example_dictionaty= {
    '키A':'값A',
    '키B':'값B',
    '키C':'값C',
}

print('# 딕셔너리의 items()함수')
print('items():',example_dictionaty.items())
print()

print('# 딕셔너리의 items() 함수와 반복문 조합하기')

for key,element in example_dictionaty.items():
    print('dictionary[{}]={}'.format(key,element))

#반복문을 사용한 리스트 생성 ---p.257
array= []

for i in range(0,20,2):
    array.append(i*i)
print(array)

#리스트 안에 for문 사용하기
array= [i*i for i in range(0,20,2)] #리스트 내포(list comprehensions)라고 부름ㄴ
print(array)
print()
# 리스트이름 = [ 표현식 for 반복자 in 반복할 수 있는 것 ]
# 리스트이름 = [ 표현식 for 반복자 in 반복할 수 있는 것 if 조건문 ]

array= ['사과','자두','초콜릿','바나나','체리']
output= [fruit for fruit in array if fruit != '초콜릿' ]
print(output)
print()

# if조건문과 여러 줄 문자열(1)
# number= int(input('정수 입력(1)> '))

# if number%2==0:
#     print('''
#           입력한 문자열은 {}입니다.
#           {}는(은) 짝수입니다.'''.format(number,number))
# else:
#     print('''
#           입력한 문자열은 {}입니다.
#           {}는(은) 홀수입니다.'''.format(number,number))
# print()

# # if 조건문과 여러 줄 문자열(2)
# number= int(input('정수 입력(2)> '))

# if number%2==0:
#     print('''입력한 문자열은 {}입니다.
#           {}는(은) 짝수입니다.'''.format((number,number)))
# else:
#     print('''입력한 문자열은 {}입니다.
#         {}는(은) 홀수입니다.'''.format((number,number)))
# print()

# # if 조건문과 긴 문자열
# number= int(input('정수 입력(3)> '))

# if number %2==0:
#     print('입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.'.format(number,number))
# else:
#     print('입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.'.format(number,number))

# 도전문제
a= [1,2,3,4,1,2,3,1,4,1,2,3]
counter= {}

for i in a:
    if i not in counter:
        counter[i]= 0
    counter[i] += 1

print(f'{a}에서')
print(f'사용된 숫자의 종류는 {len(counter)}입니다.')
print()
print(f'참고: {counter}')
print()

nucleos= input('염기 서열 입력> ')
counter={
    'a':0,
    't':0,
    'g':0,
    'c':0,
}

for nucleo in nucleos:
    counter[nucleo] +=1
for key in counter:
    print(f'{key}의 개수: {counter[key]}')

    