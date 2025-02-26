#2-3

name:str="Eric"

print(f"Hello {name}, would you like to learn some Python today?")

#2-4

name:str="Jhon"

print(name.upper)
print(name.lower)
print(name.title)

#2-5

print("Albert Einstein one said: \"A person who never makes a mistake never tried anything new\"")

#2-6

famous_person = "Albert Einstein"
quote = "\"A person who never makes a mistake never tried anything new\""

print(f"{famous_person} once said: {quote}")

#3-1

names:list = ["Riccardo", "Tiziano", "Luca", "Lorenzo"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2

print(f"sei un salame {names[0]}")
print(f"sei un salame {names[1]}")
print(f"sei un salame {names[2]}")
print(f"sei un salame {names[3]}")

#3-3

veicles:list=["Pegeot 208", "Porche 911","SH 125"]

print(f"i drive a {veicles[0]} ")
print(f"my frist veicle was a {veicles[2]}")

#3-4

guests:list=["Elon Musk","Donald Trump","Xi Jin Ping"]

print(f"dear {guests[0]} you are invited to dinner at my place")
print(f"dear {guests[1]} you are invited to dinner at my place")
print(f"dear {guests[2]} you are invited to dinner at my place")

#3-5

print(f"{guests[0]} cant make it")

guests.pop(0)
guests.append("Vladimir Putin")

print(f"dear {guests[2]} you are invited to dinner at my place")
print(f"dear {guests[0]} Elon cant make it, you are still invited to dinner at my place")
print(f"dear {guests[1]} Elon cant make it, you are still invited to dinner at my place")

#3-6

print("dear guests i foud a bigger table")

guests.insert(0,"Giorgia Meloni")
guests.insert(2,"Emmanuel Macron")
guests.insert(5,"Benito Mussolini")

for i in guests:
    print(f"dear {i} guests you are ivited to my dinner")

#3-7

print("I am a terrible organiser, only two people will be joining me")

while len(guests) > 2:
    
    removed_guests = guests.pop()
    print(f"sorry {removed_guests} you can't come anymore")
    
print(guests)    

#3-8

places:list = ["Tokyo", "New York", "Vienna", "Los Angeles","Moscaw"]

print(places)

sorted_places=sorted(places)
print(sorted_places)
print(places)

R_sorted_places= sorted (places, reverse=True)
print(R_sorted_places)
print(places)



#3-9
print(f"tonight I'm only inviting {len(guests)} people")

#3-10

#6-1

document:dict={"first_name":"Riccardo", "last_name":"Rispoli", "age":19, "city":"passoscuro"}
print(document)

#6-2

fav_numbers:dict={"Emiliano":12, "Riccardo":13, "Tiziano":25, "Luca":8, "Lorenzo":5}
for key, value in fav_numbers.items():
    print(key,value)
    
#6-3

glossary:dict={"list":"raggruppamento ordinato di dati", "tuple":"raggruppamento di dati non accessibile", \
"dict":"organizza informazioni associate a un valore e una chiave", "set": "raggruppamento disordinato di dati"}

for key, value in glossary.items():
    print(key,value)
    
#6-7    

document2:dict={"first_name":"Tiziano", "last_name":"Santoni", "age":19, "city":"Aranova"}
document3:dict={"first_name":"Lorenzo", "last_name":"Rossi", "age":19, "city":"Aranova"}

everyone:list=[document, document2, document3]

for item in everyone:
    print(f"{item}")

#6-8

pet1:dict={"animal":"dog", "owner":"bob"}
pet2:dict={"animal":"cat", "owner":"stacey"}
pet3:dict={"animal":"hamster", "owner":"mark"}

pets:list=[pet1, pet2, pet3]
for item in pets:
   print(item)

#6-9

favourite_places:dict={"Jack":"London", "Jhon":"New York", "James":"Toronto"}
for person, place in favourite_places.items():
    print(person, place)
    
#6-10

fav_numbers2:dict={"Emiliano":10, "Riccardo":33, "Tiziano":225, "Luca":83, "Lorenzo":25}
for key, value in fav_numbers.items():
    print(key,value, fav_numbers2[key])
    
#6-11



info_Roma:dict={"county":"Italy","population":"6 millions","fact":"beutiful"}
info_Madrid:dict={"county":"Spain","population":"3,2 millions","fact":"green"}
info_Berlino:dict={"county":"Germany","population":"3,4 millions","fact":"cold"}

citys:dict={"Roma":info_Roma,"Berlino":info_Berlino,"Madrid":info_Madrid}

for key, value in citys.items():
   print(key,value)

