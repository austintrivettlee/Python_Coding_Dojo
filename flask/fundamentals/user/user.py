import bankaccount


class User:
    user_list = []
    user_population = len(user_list)
    accInfo = "int_rate=.1, balance=0, account_number=0"

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = None
        if len(User.user_list) == 0:
            self.account = bankaccount.BankAccount(
                0.1, 0, 0, first_name + " " + last_name
            )
        else:
            self.account = bankaccount.BankAccount(
                0.1, 0, len(User.user_list), first_name + " " + last_name
            )

        User.user_list.append(self)

    def __str__(self):
        return f"<First Name: {self.first_name} | Last Name: {self.last_name} | Email: {self.email} | Age: {self.age} | Rewards Member: {self.is_rewards_member} | Gold Card Points: {self.gold_card_points}>"

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(
                f"Welcome to our Rewards program, you have {self.gold_card_points} points!"
            )
        else:
            print("Already a Rewards Member")
        return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
            print(
                f"You have spent {amount} leaving you with {self.gold_card_points} points left."
            )
        else:
            print("You do not have enough points. :(")
        return self

    def make_deposit(self, amount, account_type: str):
        if account_type == "main":
            self.account.deposit(amount)
        elif account_type == "savings":
            self.savings.deposit(amount)
        return self

    def make_withdraw(self, amount, account_type: str):
        if account_type == "main":
            self.account.withdraw(amount)
        elif account_type == "savings":
            self.savings.withdraw(amount)
        return self

    def show_user_balance(self):
        self.account.display_account_info()
        return self

    def create_savings(self):
        self.savings = bankaccount.BankAccount(
            0.25, 0, len(User.user_list), self.first_name + " " + self.last_name)
        return self

    def transfer_funds(self, amount, users_name, account_type):
        if self.account.balance > amount:
            self.account.withdraw(amount)
            if account_type == "main":
                User.make_deposit(users_name, amount, "main")
            elif account_type == "savings":
                User.make_deposit(users_name, amount, "savings")
        else:
            print("You do not have the funds to transfer that amount")
        return self


austin = User("Austin", "Lee", "Austintrivettlee@gmail.com", 27)
terry = User("Terry", "Lee", "terrylee@gmail.com", 30)
kayla = User("Kayla", "Lee", "kaylalee@gmail.com", 33)

bankaccount.BankAccount.show_all_accounts()
User.make_deposit(austin, 1500, "main")
User.create_savings(austin)
User.make_withdraw(austin, 500, "main")
User.make_deposit(austin, 1500, "savings")
bankaccount.BankAccount.show_all_accounts()
User.make_withdraw(austin, 500, "savings")
User.transfer_funds(austin, 500, terry, "main")
bankaccount.BankAccount.show_all_accounts()