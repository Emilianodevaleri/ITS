class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.foods = []
    
    def add_food(self, food):
        self.foods.append(food)
    
    def print_prices(self):
        for food in self.foods:
            print(f"{food.name}: ${food.price:.2f}")
    
    def get_average_price(self):
        if not self.foods:
            return 0
        return sum(food.price for food in self.foods) / len(self.foods)

pizza = Food("Pizza", 12.00)
burger = Food("Burger", 9.00)
pasta = Food("Pasta", 10.50)


menu = Menu()
menu.add_food(pizza)
menu.add_food(burger)
menu.add_food(pasta)


menu.print_prices()


print(f"Average Food Price: ${menu.get_average_price():.2f}")
