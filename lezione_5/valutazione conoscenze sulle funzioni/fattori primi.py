def prime_factors(n: int) -> list[int]:
    
    fattori_primi = []
    i = 2
    while n > 1:
        while n % i == 0:
            fattori_primi.append(i)
            n //= i
        i += 1
    return fattori_primi

print(prime_factors(60))