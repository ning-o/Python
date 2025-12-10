# 10.
q10_filename= input('파일명 입력: ')

if '2025' in q10_filename :
    print('올해 파일')
if 'report' in q10_filename :
    print('보고서 유형')
if '.csv' in q10_filename :
    print('csv 데이터 파일')
print()

# 11.
visited = '오늘 방문자 수는 350명이었고, 어제는 280명이었다.'

q11_split= visited.split()

q11_today= int(q11_split[3][0:3])
q11_yesterday= int(q11_split[5][0:3])

print(f'오늘 방문자 수 {q11_today}명')
print(f'어제 방문자 수 {q11_yesterday}명')
print(f'어제보다 오늘 {q11_today-q11_yesterday}명 증가하였습니다.')
print()


# 12.
q12_input= input('#12_채팅 입력: ')
print()

q12_result=""

if '!' in q12_input:
    print('감탄 문장')
if '?' in q12_input:
    print('의문 문장')
if len(q12_input) >=30:
    print('긴 문장')
if '0' in q12_input or '1' in  q12_input or '2' in q12_input or '3' in q12_input or '4' in q12_input or '5' in q12_input or '6' in q12_input or '7' in q12_input or '8' in q12_input or '9' in q12_input:
    print('숫자 포함 문장')
