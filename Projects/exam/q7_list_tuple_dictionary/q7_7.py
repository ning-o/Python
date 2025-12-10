# 7.
# 아래의 딕셔너리를 사용하여 전화번호부를 관리합니다. 
# phone_book = { 
# "홍길동": "010-1234-5678", 
# "김철수": "010-9876-5432", 
# "이영희": "010-5555-6666" 
# } 
# 다음의 요구사항을 수행해보세요. 
# 1. "박민수": "010-1111-2222"를 추가하시오. 
# 2. "김철수"의 번호를 "010-9999-0000"으로 수정하시오. 
# 3. "이영희"의 정보를 삭제하시오. 
# 4. 모든 이름(key)을 출력하시오. 
# 5. 모든 전화번호(value)를 출력하시오. 
# 6. 사용자로부터 이름을 입력받아, 전화번호부에서 해당 번호를 찾아 출력하시오.


phone_book = { 
"홍길동": "010-1234-5678", 
"김철수": "010-9876-5432", 
"이영희": "010-5555-6666" 
} 

print('기본 딕셔너리:',phone_book)

phone_book['박민수'] = '010-1111-2222'
print('1.박민수 추가:',phone_book)

del phone_book['이영희']
print('2.이영희 삭제:',phone_book)

for key,value in phone_book.items():
    print('모든 이름:',key)
print()
for key,value in phone_book.items():
    print('모든 전화번호:',value)

for key,value in phone_book.items():
    key_input= input('이름 입력: ')
    if key_input == key:
        print('이름:',key,'전화번호:',value)
    elif key_input != key:
        key_input= input('잘못된 이름입니다. 재입력: ')