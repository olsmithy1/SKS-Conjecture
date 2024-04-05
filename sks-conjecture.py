#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:55:33 2024

@author: Sean Smith
"""

def power_mod(base, exponent, modulus):
    """
    Compute (base^exponent) % modulus efficiently using modular exponentiation.

    Parameters:
        base (int): The base of the exponentiation
        exponent (int): The exponent
        modulus (int): The modulus

    Returns:
        int: The result of (base^exponent) % modulus
    """
    result = 1
    base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus

    return result


def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
        num (int): The number to check

    Returns:
        bool: True if num is prime, False otherwise
    """
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += w
        w = 6 - w

    return True


def is_mersenne_prime_using_sean_keith_smith(p):
    """
    Check if 2^p - 1 is a Mersenne prime using the Sean Keith Smith Conjecture.

    Parameters:
        p (int): The exponent in the Mersenne number 2^p - 1

    Returns:
        bool: True if 2^p - 1 is a Mersenne prime, False otherwise
    """
    perfect_number = (2 ** (p - 1)) * (2 ** p - 1)
    last_digit = perfect_number % 10
    return last_digit in {6, 8}


def generate_mersenne_primes_sean_keith_smith():
    """
    Generate Mersenne primes using the Sean Keith Smith test.

    Yields:
        str: Mersenne primes in the form "2 ** n - 1"
    """
    n = 2
    while True:
        if is_prime(n) and is_mersenne_prime_using_sean_keith_smith(n):
            yield f"2 ** {n} - 1"  # Use f-string for formatted output
        n += 1


# Example usage to print Mersenne primes
for mersenne_prime in generate_mersenne_primes_sean_keith_smith():
    print(mersenne_prime)
