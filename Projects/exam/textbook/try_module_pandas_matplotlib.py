# 다음 데이터를 직접 딕셔너리로 만들어서 DataFrame으로 변환하기

import pandas as pd
stu= pd.DataFrame({'철수':{'나이':23,'점수':88},'영희':{'나이':21,'점수':92},'민수':{'나이':25,'점수':57},'지영':{'나이':22,'점수':75},'호진':{'나이':24,'점수':81}})
print(stu)
print(f'평균 점수: {stu.loc["점수"].mean()}')
print()

name= list(stu.keys())
sco= stu.loc['점수'] 
hsco= sco[sco >= 80]
hsco_df= pd.DataFrame({'name': hsco.index, 'score': hsco.values})
print(hsco_df.to_string())
print()


import matplotlib.pyplot as plt
plt.rcParams['font.family']='Malgun Gothic'

colors= ['tomato' if s<60 else'gray' for s in sco ]
plt.bar(name,sco,color=colors)

plt.title('햇님반 중간고사 성적')
plt.xlabel('(이름)')
plt.ylabel('(성적)')
plt.grid(axis='y')

plt.show()

