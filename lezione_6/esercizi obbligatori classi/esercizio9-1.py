#9-1
class restaurant:
    def __init__(self, restaurant_name:str, cousine_type:str):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} è un ristorante {self.cousine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} è aperto")

Lucky_Star = restaurant("lucky star", "giapponese")

Lucky_Star.describe_restaurant()
Lucky_Star.open_restaurant()