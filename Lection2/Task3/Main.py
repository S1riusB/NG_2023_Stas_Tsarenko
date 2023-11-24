def get_numbers(digit):
    numbers = list(range(1, digit+1))
    return numbers

def get_factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def get_prime_numbers(digit):
    primes = []
    for num in range(2, digit+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

digit = int(input("Enter number: "))
numbers = get_numbers(digit)

for num in numbers:
    factors = get_factors(num)
    print(f"{num}: {factors}")

primes = get_prime_numbers(digit)
print(f"Prime numbers: {primes}")