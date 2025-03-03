#esercizio per introdurre le funzioni

# somma di interi da 1 a 10

sum:int = 0
for i in range(1, 11):
    sum += i
print("Sum from 1 to 10 is", sum)

# somma di interi da 20 a 37

sum:int = 0
for i in range(20, 38):
    sum += i
print("Sum from 20 to 37 is", sum)

# somma di interi da 35 a 49

sum:int = 0
for i in range(35, 50):
    sum += i
print("Sum from 35 to 49 is", sum)


#uso una funzione

def sum(a:int, b:int):

    result:int = 0
    for i in range(a,b+1):
        result = result + i
    
    return result


mysum = sum(1, 10)
print(f"Sum from 1 to 10 is {sum(1, 10)}")


#funzione subctract

def subtract(a:int, b:int):
    result:int = a - b
    return result

myresult = subtract(8, 1)
print(myresult)