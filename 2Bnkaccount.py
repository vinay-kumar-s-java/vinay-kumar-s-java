class bankaccount:
    def __init__(self,accountNo,balance):
        self.accountNo=accountNo
        self.balance=balance
    def deposite(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        if(self.balance>0 and amount > self.balance):
            print("balance insuffient")
            return f"balance={self.balance}"
        self.balance=self.balance-amount
        return self.balance
user1=bankaccount(2345,0)

print(user1.deposite(1000))
print(user1.deposite(5000))
print(user1.withdraw(2000))


