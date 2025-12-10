# 3.
# 아래와 같이 학생들의 성적을 받아서 score_list 라는 이름의 리스트에 저장하고, 
# 평균을 구하는 프로그램을 작성해보자. (평균은 소수점 2자리까지만 표시) 
# 단, 입력값이 0~100 사이가 아니면 다시입력하도록 하시오.

# 실행결과 예시) 
# 학생의 수를 입력하시오 : 2 
# 학생 1의 성적을 입력하세요 : 20 
# 학생 2의 성적을 입력하세요 : 110 
# 잘못된 성적입니다. 다시 입력하시오. 
# 학생 2의 성적을 입력하세요 : 30 
# —-------------------- 
# 학생 1의 성적 : 20 
# 학생 2의 성적 : 30 
# —-------------------- 
# 성적 평균은 25.00 입니다. 

student_counter= int(input('학생 수 입력: '))
score_list= []
score_dic= {}
print()
for stu_count in range(student_counter):
        stu_rec= int(input(f'학생{stu_count+1} 성적 입력: '))
        score_list.append(stu_rec)
        score_dic[stu_count+1] = stu_rec
        if stu_rec <0 or stu_rec > 100: 
            print(int(input(f'잘못된 성적입니다. 학생{stu_count+1} 재입력: ')))
print()
for dic_1,dic_2 in score_dic.items():
    print(f'학생 {dic_1}의 성적 : {dic_2}')
print()
        
score_total= sum(score_list)
print('성적 평균은 {:.2f}입니다.'.format(score_total/len(score_list)))
print()