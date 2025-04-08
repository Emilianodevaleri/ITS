def sum(n:int) -> None:
    sum:int = 0
    if n < 0 :
        print("Error! Inserted number is negative!")
        return None

    else:
        while n >= 0:
            sum = sum + n 
            n = n - 1
    print(sum)

sum(-5)
sum(5)





        