class BankAccount:
    total_accounts = 0
    all_accounts = []
    def __init__(self, int_rate, balance, account_number, full_name): 
        self.int_rate = int_rate
        self.balance = balance
        self.account_number = account_number
        self.full_name = full_name
        BankAccount.total_accounts += 1
        BankAccount.all_accounts.append(self)

    def __str__(self):
        return f"Account: {self.account_number} Name:{self.full_name} | Balance: ${self.balance} | Interest Rate: {self.int_rate}%"

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.full_name}, Your new balance is ${self.balance} after deposit for account id: {self.account_number}")
        return self
    def withdraw(self, amount):
        if(self.balance - amount < 0):
            print(f"{self.full_name}, You do not have enough funds to withdraw ${amount}.")
        else:
            self.balance -= amount
            print(f"{self.full_name}, Your new balance is ${self.balance} after withdrawal for account id: {self.account_number}")
        return self
    # def tranfer(self, amount, other):
    #     se
    def display_account_info(self):
        print(f"{self.full_name}, Your balance is: ${self.balance} for account id: {self.account_number}")
        return self
    def yield_interest(self):
        if(self.balance > 0):
            print(f"Interest paid from initial balance of {self.balance}")
            print(f"Your total interest is: ${(self.balance * self.int_rate )}")
            self.balance += self.balance * self.int_rate
        else:
            print("No interest can be given at this time.")
        return self
    @classmethod 
    def show_all_accounts(cls):
        for account in cls.all_accounts:
            print(account)

