# 랜덤하게 1000명의 키와 몸무게 만들기
import random

name_2= list('영조라희경홍현')
name_1= list('보영나지은이재')
first_name= list('김이박조유탁')
first_name2= ['서문']
with open ('files\\info.txt','w',encoding='UTF-8') as file:
    for i in range(1000):
        if random.random() <0.8:
            last_name = random.choice(first_name)
        else:
            last_name = random.choice(first_name2)
        full_name= last_name + random.choice(name_1) + random.choice(name_2)

        weight= random.randrange(40,120)
        height= random.randrange(140,210)

        file.write('{},{},{}\n'.format(full_name,weight,height))