"""
    날짜 : 2020/06/24
    이름 : 이성진
    내용 : 클래스 교재 p183
"""
#클래스 정의
class Account:
    # 멤버변수(__init__ 생성자에서 선언)
    def __init__(self, bank, id, name, money):
        self.bank = bank
        self.id = id
        self.name = name
        self.money = money

    # 멤버함수
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money

    def show(self):
        print('---------------------')
        print('은 행 명 :', self.bank)
        print('계좌번호 :', self.id)
        print('입 금 주 :', self.name)
        print('현재잔액 :', self.money)
        print('---------------------')

#객체생성
kb = Account('국민은행', '101-12-1111', '김유신', 10000)
wr = Account('우리은행', '101-12-2222', '김춘추', 10000)

kb.deposit(30000)
kb.withdraw(5000)
kb.show()

wr.deposit(25000)
wr.withdraw(7000)
wr.show()