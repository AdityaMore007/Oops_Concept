## Create Account class with 2 Attributes- balance & account.no
## Create methods for Debit,Credit and Printing the balance.

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc
        
    #Debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was Debited")
        print("Total Balance =", self.get_balance())
    
    def Credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was Credited ")
        print("Total Balance =", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
        
acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.Credit(50000)