# 리스트 연산자 ----p.196
list_a= [1,2,3]
list_b= [4,5,6]

print('# 리스트')
print('list_a=',list_a)
print('list_b=',list_b)
print('list_a + list_b=',list_a+list_b)
print('list_a x 3=',list_a*3)

print('list_a길이:',len(list_a))
print('-'*30,'\n')

# 리스트에 요소 추가하기 ---p.198
list_a.append(4)
print(list_a)

list_a.insert(0,10)
print(list_a)
print('-'*30,'\n')

# 리스트 요소 하나 제거하기
del list_a[2]
print(list_a)

list_a.pop(1)
print(list_a)

# list_a.clear() # 모두 제거
# print(list_a)

list_a.sort() # 순서대로 정렬
print(list_a)

print('-'*30,'\n')

# 반복문과 리스트 ---p.209
array= [273,32,103,57,52]

for element in array:
    print(element)
print()

# 2차원 리스트에 반복문 한번 사용하기
list_of_list=[
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for items in list_of_list:
    print(items)
print()
for items in list_of_list:
    for item in items:
        print(items)
print('-'*30,'\n')

# 4-1도전문제 --p.214
# 100이상의 숫자만 출력되게하기
numbers = [273,103,5,32,65,9,72,800,99]

for num in numbers:
    if num>=100:
        print(num)
print()
# 홀짝 구분 출력
numbers = [273,103,5,32,65,9,72,800,99]

for num in numbers:
    if num%2==0:
        print(num,'는 짝수입니다.')
    elif num%2!=0:
        print(num,'는 홀수입니다.')
print()
# 자릿수 구분
for num in numbers:
    print(f'{num}은 {len(str(num))}자릿수 입니다.')
print('-'*30,'\n')

numbers = [1,2,3,4,5,6,7,8,9]
ouput= [[],[],[]]

for number in numbers:
    ouput[((number+2)%3)].append(number)
print(ouput)
print('-'*30,'\n')

numbers = [1,2,3,4,5,6,7,8,9]
for i in range(0,len(numbers)//2):
    j=(i*2)+1
    print(f'i={i}, j={j}')
    numbers[j]= numbers[j]**2
print(numbers)
print('-'*30,'\n')

# ---p.227
pets=[
    {'name':'구름','age':5},
    {'name':'초코','age':3},
    {'name':'아지','age':1},
    {'name':'호랑이','age':1},
]
print('#우리동네 애완동물들')
for pet in pets:
    print(pet['name'],pet['age'],'살')
print()

numbers= [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter= {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number]+1
    else:
        counter[number] = 1
print(counter)
print('-'*30,'\n')

# --p.

character= {
    'name':'기사',
    'level': 12,
    'items':{
        'sword':'불꽃의 검',
        'armor':'풀ㄹ플레이트'
    },
    'skill':['베기','세게 베기','아주 세게 베기']
}
for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key,":",character[key][[small_key]])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key,':',item)
    else:
        print(key,":",character[key])