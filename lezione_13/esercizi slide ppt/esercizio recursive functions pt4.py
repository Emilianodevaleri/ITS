def sumInRange(a:int, b:int) -> int:

    if a > b:

        temp:int = a

        a = b
        b = temp

    sum:int = 0

    while b >= a:
        sum = sum + b
        b = b - 1

    return int(sum)

print(sumInRange(a = 5, b = 10))
print(sumInRange(a = 10, b = 5))
