class User:
    # ! CONSTRUCTOR FUNCTION!!! CREATES THE INSTANCE OF AN OBJECT
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account = BankAccount(interest_rate = 0.01, balance = 0)

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount 
        return self


class BankAccount:
    accounts = []
    def __init__(self, balance, interest_rate):
        self.balance = balance 
        self.interest_rate = 0.01
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate) 
        return self

    @classmethod
    def user_details(cls):
        for account in cls.accounts:
            account.display_account_info()


heav = User("Heav", "Griffith", 20)
david = User("David", "Griffith", 23)
steve = User("Steve", "Griffith", 65)



heav.account.deposit(100).deposit(100).deposit(100).withdraw(100).display_account_info()
heav.transfer_money(steve, 10000)
david.account.deposit(200).deposit(200).withdraw(100).withdraw(10000).display_account_info()
steve.account.deposit(100000).withdraw(100000000000000).withdraw(10000000000000000000000).withdraw(10000000000000000000000).display_account_info()
print(heav.account.balance)
print(steve.account.balance)
















































