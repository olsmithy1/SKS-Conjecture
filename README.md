Mersenne Prime Generator

This Python script provides a Mersenne prime generator based on the Sean Keith Smith test. It includes functions to efficiently compute potential Mersenne primes and check for primality using modular exponentiation and prime checking algorithms.
The algorithm included is based on my own observations regarding the nature and correlation of mersenne primes and perfect numbers. Euler and possibly Euclid made these same observations as well. The conjecture states that Mersenne primes correspond closely to even perfect numbers ending in 6 or 8. It should be noted that this code generates probabilistic mersenne primes based on known attributes. That does not mean that all numbers produced by it, will be Mersenne primes and a strong deterministic test should be used for higher certainty such as a Lucas-Lehmer test. Although for the purposes of a sieve for those types of numbers it is incredibly efficient methodology. 

Features

    Mersenne Prime Generation: Generates Mersenne primes of the form 2^p - 1 based on the Sean Keith Smith test.
    Efficient Computations: Utilizes modular exponentiation for fast computation of (base^exponent) % modulus.
    Prime Number Checking: Implements efficient algorithms to check whether a given number is prime.
    Sean Keith Smith Test: Validates potential Mersenne primes using the Sean Keith Smith conjecture.

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
--

Mersenne Prime Conjecture - Proof by Contradiction

This Python code explores the Sean Keith Smith Conjecture on Mersenne primes using proof by contradiction. The conjecture states that Mersenne primes (of the form 2^n - 1) correspond to even perfect numbers ending in 6 or 8.

Functionality:

    The disprove_sks_conjecture function analyzes a given even perfect number (p) to see if it contradicts the conjecture.
    It checks the last digit of p and performs casework to identify potential contradictions based on divisibility rules.
    If the analysis reveals a scenario where the corresponding Mersenne prime (M) cannot be prime (due to divisibility properties), it indicates a contradiction and strengthens the conjecture for that specific case.

How to Use:

    Clone or download this repository.
    The code assumes you have Python installed.
    Edit the even_perfect_num variable in the example usage section of the code with a hypothetical even perfect number that doesn't end in 6 or 8 (if one exists).
    Run the script using python disprove-sks.py.

Note:

    This code demonstrates a simplified version of the proof by contradiction logic for educational purposes. A formal mathematical proof would require more rigorous reasoning and notation.
    Finding a contradiction for a specific even perfect number strengthens the conjecture but doesn't guarantee it holds true universally.
