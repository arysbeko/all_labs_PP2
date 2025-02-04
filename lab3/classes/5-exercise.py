class Bank:
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def get_balance(self):
        return self.balance
    
    def get_owner(self):
        return self.owner
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Current balance: {self.balance}"
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            return f"Insufficient funds. Current balance: {self.balance}"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. Current balance: {self.balance}"



bank = Bank("Arysbek", 1000)


print("Owner:", bank.get_owner())  
print("Initial balance:", bank.get_balance())  
print(bank.deposit(1000)) 
print(bank.withdraw(3000)) 
print(bank.withdraw(2000))