# Problem 9: Find prime numbers in a list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [int(num.strip()) for num in input().split(',')]
primes = tuple(num for num in numbers if is_prime(num))
print(f"Prime numbers: {primes}")