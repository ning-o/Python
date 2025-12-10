# 숫자로 변환되는 것들만 리스트에 넣기 --p.368
list_input_a=['52','273','32','스파이','103']

list_num=[]
for item in list_input_a:
    try:
        float(item)
        list_num.append(item)
    except:
        pass

print(list_input_a)
print(list_num)
print()

