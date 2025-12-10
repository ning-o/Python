# 반복문으로 파일 한 줄씩 읽기----p.332
# 앞에 랜덤값으로 만든 천명의 정보 파일을 활용한 예제

taget_name= '서문나라'

with open('files\\info.txt','r',encoding='UTF-8') as file:

    for line in file:

        pp = [p.strip() for p in line.strip().split(',')]
        if len(pp) != 3:
            continue
        full_name, weight, height = pp

        if (not full_name) or (not weight) or (not height):
            continue
        full_name= full_name.strip()

        bmi = int(weight) / ((int(height)/100) **2)
        result= ""

        if  25 <= bmi:
            result= '과체중'
        elif 18.5 <= bmi:
            result= '정상 체중'
        else:
            result= '저체중'

        # if "저체중" != result:
        #     continue

        print('\n'.join([
            '이름: [{}]',
            '몸무게: [{}]',
            '키: [{}]',
            'BMI: [{:.2f}]',
            '결과: [{}]'
        ]).format(full_name,weight,height,bmi,result))

        if full_name == taget_name:
             break
        print()