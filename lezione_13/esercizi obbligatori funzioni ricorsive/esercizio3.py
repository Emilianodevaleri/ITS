#3

def recursiveFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursiveFactorial(n - 1)
    
print(recursiveFactorial(5))