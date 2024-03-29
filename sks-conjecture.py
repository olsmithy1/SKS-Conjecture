#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:55:33 2024

@author: Sean Smith
"""

def is_perfect_number(num):
    """
    Check if a number is a perfect number.

    Parameters:
        num (int): The number to check

    Returns:
        bool: True if num is a perfect number, False otherwise
    """
    if num <= 1:
        return False

    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i

    return divisors_sum == num


def sks_test(n):
    """
    Perform the SKS Test for Mersenne primes.

    Parameters:
        n (int): The exponent in the Mersenne number 2^n - 1

    Returns:
        bool: True if 2^n - 1 is a Mersenne prime based on the SKS Conjecture, False otherwise
    """
    # Calculate the n-th triangular number
    triangular_num = (n * (n + 1)) // 2

    # Check if the triangular number is a perfect number
    if not is_perfect_number(triangular_num):
        return False

    # Check if the last digit of the triangular number is 6 or 8
    last_digit = triangular_num % 10
    if last_digit not in {6, 8}:
        return False

    # If the triangular number is a perfect number ending in 6 or 8,
    # then according to SKS Conjecture, 2^n - 1 is a Mersenne prime
    return True


def generate_sks_mersenne_primes():
    """
    Generate Mersenne primes using the SKS Test.

    Yields:
        str: Mersenne primes in the format "2^n - 1"
    """
    n = 1
    while True:
        if sks_test(n):
            yield f"2^{n} - 1"
        n += 1


# Example usage to print SKS Mersenne primes
for sks_mersenne_prime in generate_sks_mersenne_primes():
    print(sks_mersenne_prime)
