class BankAccount: 
    # 인스턴스 초기화 
    def __init__(self, acc_number, acc_holder, balance):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance
        print(f'계좌가 개설되었습니다.\n계좌 번호: {acc_number}\n소유자: {acc_holder}\n초기 잔액: {balance}')

    # 계좌에 금액 입금 
    def deposit(self, money):
        self.balance += money 
        print(f'{money}원이 입금되었습니다. 현재 잔액: {self.balance}원')
    
    # 계좌에 금액 출금
    def withdraw(self, money):
        if self.balance > money: 
            self.balance -= money
            print(f'{money}원이 출금되었습니다. 현재 잔액 : {self.balance}원')
        else:
            print(f'잔액보다 많은 금액을 출금할 수 없습니다! 현재 {money}원을 출금할 수 없습니다.')
    
    # 현재 계좌에 잔액 반환
    def get_balance(self):
        return self.balance 
    
# 사용 예시
if __name__ == "__main__":
    my_account = BankAccount("123-456-789", "김철수", 100000)
    my_account.deposit(50000)
    my_account.withdraw(20000)
    print(f"현재 잔액: {my_account.get_balance()}원")

"""
생각보다 그렇게 어렵지는 않았음. 계좌에서 금액을 출금할 때 경우의 수를 나누는 과정을
잘 생각했으면 어렵지 않게 풀 수 있었음. 
"""