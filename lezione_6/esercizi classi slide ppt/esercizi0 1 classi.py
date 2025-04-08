

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:
    print("alice è più grande di bob")
else:
    print("bob è più grande di alice")


mats = Person("Mats M.", 37)
paulo = Person("Paulo M.", 29)
sofie = Person("Sofie W.", 19)

people:list = [alice, bob, mats, paulo, sofie]

giovane = people[0]

for person in people:
    if person.age < giovane.age:
        giovane.age = person.age
        giovane.name = person.name

print(f"la persona più giovane è {giovane.name} e ha {giovane.age} anni")