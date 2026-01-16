class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal")

    def __del__(self):
        print("Account deleted")


acc = BankAccount(12345, 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.withdraw(7000)
