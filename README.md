Mersenne Prime Generator

This Python script provides a Mersenne prime generator based on the Sean Keith Smith test. It includes functions to efficiently compute Mersenne primes and check for primality using modular exponentiation and prime checking algorithms.
Features

    Mersenne Prime Generation: Generates Mersenne primes of the form 2^p - 1 based on the Sean Keith Smith test.
    Efficient Computations: Utilizes modular exponentiation for fast computation of (base^exponent) % modulus.
    Prime Number Checking: Implements efficient algorithms to check whether a given number is prime.
    Sean Keith Smith Test: Validates Mersenne primes using the Sean Keith Smith conjecture.

Contents

    power_mod(base, exponent, modulus): Efficiently computes (base^exponent) % modulus using modular exponentiation.
    is_prime(num): Checks whether a given number num is prime.
    is_mersenne_prime_sks(p): Tests if 2^p - 1 is a Mersenne prime based on the Sean Keith Smith test.
    generate_mersenne_primes(): Generator function to yield Mersenne primes indefinitely.

Usage

To use the Mersenne prime generator, run the script and iterate through the generated primes:

python sks-conjecture.py

# Example usage to print Mersenne primes
for mersenne_prime in generate_mersenne_primes():
    print(mersenne_prime)

How It Works

The generate_mersenne_primes() function continuously generates Mersenne primes using the Sean Keith Smith test. It checks each prime number p for Mersenne primality using the formula 2^(p-1) * (2^p - 1).
Requirements

    Python 3.x
