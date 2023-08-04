class User:

    user_population = 0

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        User.user_population += 1

    def __str__(self):
        return f"<First Name: {self.first_name} | Last Name: {self.last_name} | Email: {self.email} | Age: {self.age} | Rewards Member: {self.is_rewards_member} | Gold Card Points: {self.gold_card_points}>"

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

    def enroll(self):
        if(self.is_rewards_member == False):
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"Welcome to our Rewards program, you have {self.gold_card_points} points!")
        else:
            print("Already a Rewards Member")
        return self

    def spend_points(self, amount):
        if(amount < self.gold_card_points):
            self.gold_card_points = self.gold_card_points - amount
            print(f"You have spent {amount} leaving you with {self.gold_card_points} points left.")
        else:
            print("You do not have enough points. :(")
        return self

austin = User("Austin", "Lee", "Austintrivettlee@gmail.com", 27)
austin2 = User("Austin", "Lee", "Austintrivettlee@gmail.com", 27)
austin3 = User("Austin", "Lee", "Austintrivettlee@gmail.com", 27)

User.display_info(austin).enroll().spend_points(150)
print(User.user_population)




