# Class : GPT과제

# 1). Student
# introduce() → “저는 000이고 학번은 000입니다.” 출력
# is_passed() → 60점 이상이면 True, 아니면 False 반환

class Student:
    def __init__(self, name, student_id, grade):
        self.name= name
        self.student_id= student_id
        self.grade= grade

    def introduce(self):
        print(f'저는 {self.name}이고 학번은 {self.student_id}입니다.')

    def is_passed(self, score):
        self.score= score
        if score >= 80:
            print('학업 성적이 우수합니다.')
        elif score >= 60:
            print('평범')
        else:
            print('우우~~')

stu= Student('sam', 251205, 3)
# stu.introduce()
# stu.is_passed(92)

# 2). BankAccount
# deposit(amount) → 입금
# withdraw(amount) → 잔액보다 적으면 출금, 아니면 경고 메시지
# check_balance() → 잔액 출력

# accounts= 계좌
# amount= 입금

class Bank:
    def __init__(self):
        self.accounts= {}

    def desposit(self, name, amount):
        if name not in self.accounts:
            self.accounts[name]= amount
        
        else:
            self.accounts[name] += amount
        print(f'{name}님의 계좌에 {amount}원 입금')
        print(f'{name}님의 현재 잔액: {self.accounts[name]:,}원')
        print()

    def withdrawal(self, name, amount):
        if name not in self.accounts:
            print('생성된 계좌가 없습니다.')
            return
        elif self.accounts[name] < amount:
            print('잔액이 부족합니다.')
            return

        self.accounts[name] -= amount
        print(f'{name}님의 계좌에 {amount}원 출금')
        print(f'{name}님의 현재 잔액: {self.accounts[name]:,}원')
        print()

bank= Bank()

# bank.desposit('jihee',3500)
# bank.withdrawal('jihee',1000)
# bank.desposit('somang', 7000)
# bank.desposit('junyoung',125000)       

# 3). Charascter
# attack_target(target) → target.hp 감소
# Warrior, Mage 클래스 만들기 (상속)
# 각각 특별한 공격 메서드 1개씩 추가
# 캐릭터 두 개를 만들어 서로 공격 주고받기 시뮬레이션
import random
class Character:
    def __init__(self, nick, hp=100):
        self.nick= nick
        self.hp= hp

    def attack(self, target):
        damage= random.randrange(10,30)
        target.hp -= damage
        print(f'{target.nick}이 공격받음 -{damage} 현재hp: {target.hp}')

    def portion(self):
        self.hp += 10
        print(f'{self.nick}가 포션사용!! 현재 hp:{self.hp}')


class Warrior(Character):
    def __init__(self, nick, hp=100):
        super().__init__(nick, hp)
        self.hp= hp+50
        print(f'전사 패시브 발동!! hp상승... 현재 hp: {self.hp}')
        print()

    def attack(self, target, w_at=0):
        super().attack(target)
        self.w_at= w_at
        w_at= random.randrange(20,40)
        target.hp -= w_at
        print(f'{target.nick}이 전용 스킬 "창 찌르기"에 당했습니다. -{w_at} 현재hp: {target.hp}')

    def portion(self):
        super().portion()

hong= Warrior('hong')
sam= Character('sam')
hong.attack(sam)






        



        