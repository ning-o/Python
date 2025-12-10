import datetime

now= datetime.datetime.now()

print(f'{now.year}년{now.month}월{now.day}일{now.hour}시{now.minute}분{now.second}초')
print()


month_input= int(input('지금이 몇월인지 입력하세요: '))

if 3<= month_input <= 5 :
    print(f'지금은 {month_input}월로 봄입니다.')

if 6<= month_input <= 8 :
    print(f'지금은 {month_input}월로 여름입니다.')

if 9<= month_input <=10 :
    print(f'지금은 {month_input}월로 가을입니다.')

if 11<= month_input <= 12 :
    print(f'지금은 {month_input}월로 겨울입니다.')

if 1<= month_input <= 2 :
    print(f'지금은 {month_input}월로 겨울입니다.')


now= datetime.datetime.now()
month= now.month

if 3 <= month <= 5 :
    print('현재는 봄입니다.')
elif 6 <= month <= 8:
    print('현재는 여름입니다.')
elif 9 <= month <= 11:
    print('현재는 가을입니다.')
else:
    print('현재는 겨울입니다.')










