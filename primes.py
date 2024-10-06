"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    list = []
    number = 0  
    if number_of_primes<= 0:
        raise ValueError(f"cannot have a {number_of_primes} prime number")
    while len(list) < number_of_primes:
        if is_prime(number):
            list.append(number)
        number += 1
    
    return list


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


print(primes(-1))