# 5.
# 아래와 같은 학생 점수 리스트가 있습니다. 
# scores = [85, 90, 78, 92, 68] 
# 다음을 수행하세요. 
# 1. scores의 평균 점수를 구하시오. 
# 2. 가장 높은 점수와 가장 낮은 점수를 출력하시오. 
# 3. 점수를 오름차순으로 정렬한 새 리스트를 만드시오. 
# 4. 80점 이상인 점수만 모은 리스트를 만드시오. 
# 5. 리스트 내의 점수를 전부 5점씩 올리는 코드를 작성해보세요. 

scores = [85, 90, 78, 92, 68]

print(f'평균 점수: {sum(scores)/len(scores)}')
print(f'가장 높은 점수: {max(scores)}\n가장 낮은 점수: {min(scores)} ')
scores.sort()
print('오름차순 정렬:',scores)

scores_80= []

for sco in scores:
    if sco >= 80:
        scores_80.append(sco)
print('80점 이상인 점수:',scores_80)

scores_5=[]

for score in scores:
    scores_5.append(score+5)
print(scores_5)
