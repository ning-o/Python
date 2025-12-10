# 5. 셀프 과제
# 게임 데이터 분석해서 KDA 계산하기

# game_1= []
# game_2= []
# game= []

# with open('files/game.csv','r',encoding='utf-8') as file:
#     rd_f= file.readlines()[1:]
#     for f in rd_f:
#         line= f.strip().split(',')
#         game= line[0]
#         if game == '1':
#             game_1.append(line)
#         else:
#             game_2.append(line)
            
# print(game_1)
# print(game_2)

kda_list= []
nick= []

with open('files/game.csv','r',encoding='utf-8') as file:
    rd= file.readlines()[1:]
    for f in rd:
        ff= f.strip().split(',')
        
        nick.append(ff[1])
        k= int(ff[2])
        d= int(ff[3])
        a= int(ff[4])

        if d == 0:
            d= 1

        kda= (k+a)/d
        kda_list.append(kda)

kda_dict= {}
    for aa in 

