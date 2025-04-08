def countdown(n:int) -> None:
    if n >= 0 :
        while n:
            print(n) 
            n = n - 1
    else:
        print("error! insert positive number")

countdown(-5)

countdown(5)


