class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print("User Info:")
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("City:", self.city)
        print()

    def greet_user(self):
        print("Hi", self.first_name + "!", "Nice to see you!\n")



user1 = User("Lorenzo", "Rossi", 20, "lorenzorossi@example.com", "Roma")
user2 = User("Anna", "Bianchi", 30, "annabianchi@example.com", "Milano")
user3 = User("Luca", "Esposito", 25, "lucaesposito@example.com", "Napoli")


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
