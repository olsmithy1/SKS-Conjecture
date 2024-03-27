def disprove_sks_conjecture(p):
  """
  This function attempts to disprove the Sean Keith Smith conjecture by contradiction for a given even perfect number (p).

  Args:
      p: The even perfect number to analyze.

  Returns:
      bool: True if a contradiction is found (disproving the conjecture for this p), False otherwise.
  """

  # Check if the last digit of p is not 6 or 8 (assuming the opposite of the conjecture)
  last_digit = p % 10
  if last_digit not in (6, 8):
    # Analyze cases based on the last digit
    if last_digit == 0:
      # Case 1: p ends in 0 (multiple of 10, thus also multiple of 5)
      if p % 5 == 0:
        n = p.bit_length() - 1  # Extract exponent (n-1) from p (2^(n-1) * M)
        if n % 5 == 0:
          # M (2^n - 1) would be even (contradiction with primality)
          print(f"Contradiction! Even perfect number {p} (Mersenne prime 2^{n} - 1) is even (not prime).")
          return True
    else:
      # Cases 2 & 3: p ends in 2 or 4 (not necessarily divisible by 4)
      if p % 4 != 0:
        n = p.bit_length() - 1  # Extract exponent (n-1) from p (2^(n-1) * M)
        if (n + 1) % 4 != 0:
          # M (2^n - 1) wouldn't be guaranteed prime (contradiction)
          print(f"Contradiction! Even perfect number {p} (Mersenne prime candidate 2^{n} - 1) might not be prime.")
          return True
  return False

# Example usage: 
even_perfect_num = 90  # Replace with an even perfect number NOT ending in 6 or 8 (if one exists)
contradiction_found = disprove_sks_conjecture(even_perfect_num)

if not contradiction_found:
  print("No contradiction found for this even perfect number (doesn't disprove the conjecture for all cases).")
