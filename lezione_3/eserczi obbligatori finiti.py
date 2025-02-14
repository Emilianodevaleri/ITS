#4-1
pizze:list=["Margherita", "Diavola","Capricciosa"]

for pizza in pizze:
    print(f"I love {pizza} pizza")
    
print("I really love pizza")

#4-2
animals:list=["dog","cat","dragon"]

for animal in animals:
    print(animal)
    
for animal in animals:
    print(f"a {animal} is popular")
    
print("all of these animal are popular")

#4-3

numbers:list=[]

for i in range(1,20+1):
    numbers.append(i)
    print(i)

#4-4
'''
one_million:list=[i for i in range(1,1000000+1)]
print(one_million)  

convertito in commento per evitare lag   '''

#4-5

one_million:list=[i for i in range(1,1000000+1)]

print(min(one_million))
print(max(one_million))

print(sum(one_million))

#4-6

odd_numbers:list=[x for x in range(1,20,2)]
print(odd_numbers)

#4-7

multiple_of_3:list=[y*3 for y in range(1,10+1)]
print(multiple_of_3)

#4-8

cubes:list=[]

for cube in range(1,10+1):
    cubes.append(cube**3)
    
print(cubes)

#4-9

cubes2:list=[c**3 for c in range(1,10+1)]
print(cubes)

#4-10

animals:list=["dog","cat","dragon","lion","shark","eagle","robin","octopus","tiger"]

first3:list=animals[:2+1]
middle3:list=animals[3:5+1]
last3:list=animals[6:9+1]

print(f"The first three items in the list are {first3}")
print(f"Three items from the middle of the list are:{middle3}")
print(f"The last three items in the list are:{last3}")

#4-11

pizze:list=["Margherita", "Diavola","Capricciosa","quattro formaggi"]
friend_pizzas:list=["Margherita", "Diavola","Capricciosa","ortolana"]


print("my favorite pizzas are:")
for p in pizze:
    print(p)

print("My friend’s favorite pizzas are:")
for f in friend_pizzas:
    print(f)

#5-1

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#5-3

alien_color="green"
if alien_color=="green":
    print("player earned 5 points")
    
else:
    pass

#5-4

alien2_color="yellow"

if alien2_color=="green":
    print("player just earned 5 points for shooting the alien")
    
else:
    print("player just earned 10 points")
    
#5-5

alien3_color="red"

if alien3_color=="green":
    print("player just earned 5 points for shooting the alien")
    
elif alien3_color=="yellow":
    print("player just earned 10 points")

else:
    print("player earned 15 points")

#5-6

person_age=20

if person_age < 2:
    print("person is a baby")
elif 2 <= person_age < 4:
    print("person is a toddler")
elif 4 <= person_age < 13:
    print("person is a kid")
elif 13 <= person_age < 20:
    print("person is a teenager")
elif 20 <= person_age < 65:
    print("person is a adult")
elif person_age >= 65:
    print("person is elder")

#5-7

favourite_fruits:list=["apple","pear","mango","watermelon","peach"]

if "mango" in favourite_fruits:
    print ("i really like mangos")
else:
    print ("i don't like mangos")

if "banana" in favourite_fruits:
    print("i really like bananas")
else:
    print("i don't like bananas")

#5-8

usernames:list=["slayer","camper","admin","user","hater"] 

for username in usernames:
    
    if username is "admin":
        print("Hello admin, would you like to see a status report?")
        
    else:
        print(f"Hello {username}, thank you for logging in again.")
        
#5-9

if len(usernames) == 0:
    print("We need to find some users!")  
    
#5-10

current_users:list = ["axe", "bat", "mac", "dack", "trev"]

current_users_caps:list = [user.upper() for user in current_users]

new_users:list = ["AXE", "ilme", "boss", "trev", "key"]

for user in new_users:
    
    if user in current_users:
        print("username has already been used, enter a new username")
        
    elif user in current_users_caps:
        print("username has already been used, enter a new username")
        
    else:
        print("username is available")

#5-11

numbers1_9:list=[x for x in range(1,10)]

for x in numbers1_9:
    
    if x == 1:
        print(f"{x}st")
        
    elif x == 2:
        print(f"{x}nd")
    
    elif x == 3:
        print(f"{x}rd")
        
    else:
        print(f"{x}th")