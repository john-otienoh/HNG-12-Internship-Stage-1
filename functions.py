"""
Contains all functions for the api attributes
"""
def is_perfect(num: int) -> bool:
    "Checks if a number is a perfect number"
    summ, i = 0, 1
    while i < num:
        if num % i == 0:
            summ += i
        i += + 1
    return True if summ == num else False

def is_prime(num: int) -> bool:
    "Checks if a number is a prime number"
    if num <= 1:
        return 'false'
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_sum(num: int) -> int:
    "Return sum of digits"
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    return summ

def is_armstrong(num: int) -> bool:
    "Check if a number is an armstrong number"
    n = num
    s = 0
    while n > 0:
        digit = n % 10
        s += digit ** 3
        n //= 10
    return True if s == num else False

def properties(num: int) -> list:
    "Return properties of the number"
    features = []
    if is_armstrong(num):
        features.append("armstrong")
    if num % 2 == 0:
        features.append("even")
    else:
        features.append("odd")
    return features
