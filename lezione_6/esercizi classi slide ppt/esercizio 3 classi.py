class Animal:
    def __init__(self, name:str, specie:str, zampe:int):
        self.name = name
        self.specie = specie
        self.zampe = zampe

    def set_legs(self, new_zampe):
        self.zampe = new_zampe

    def get_legs(self):
        return self.zampe 

def print_info(self):
    print(f"il {self.name} è un {self.specie} e ha {self.zampe} zampe")

     

gatto = Animal("gatto", "felino", 4)
granchio = Animal("granchio", "crostaceo", 6)

print_info(gatto)
print_info(granchio)

granchio.zampe = 8

print_info(granchio)

granchio.set_legs(6)
granchio.get_legs

print_info(granchio)


