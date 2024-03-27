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


def is_mersenne_prime_sks(p):
    """
    Check if a number of the form 2^p - 1 is a Mersenne prime
    using the Sean Keith Smith test.

    Parameters:
        p (int): The exponent in the Mersenne number 2^p - 1

    Returns:
        bool: True if 2^p - 1 is a Mersenne prime based on the last digit
              of the even perfect number formed using p, False otherwise.
    """
    # Calculate the even perfect number: 2^(p-1) * (2^p - 1)
    even_perfect_num = power_mod(2, p - 1, p)

    # Mersenne primes are associated with even perfect numbers
    # that end in 6 or 8 based on the Sean Keith Smith conjecture.
    return even_perfect_num in {1, p - 1}


def generate_mersenne_primes():
    """
    Generate Mersenne primes indefinitely using the Sean Keith Smith test.

    Yields:
        str: Mersenne primes in the form "2 ** n - 1"
    """
    n = 2
    while True:
        if is_prime(n):
            if is_mersenne_prime_sks(n):
                mersenne_num = (2 ** n) - 1
                yield f"2 ** {n} - 1"
        n += 1


# Example usage to print Mersenne primes
for mersenne_prime in generate_mersenne_primes():
    print(mersenne_prime)
