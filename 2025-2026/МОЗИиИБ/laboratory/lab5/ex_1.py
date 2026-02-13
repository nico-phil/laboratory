import random

def is_probable_prime_fermat(n: int, rounds: int = 10) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        if gcd(a, n) != 1:
            return False  # composite
        if pow(a, n - 1, n) != 1:
            return False  # composite
    return True  # probably prime


def gcd(a: int, b: int) -> int:
    """Classic Euclid GCD using remainders."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a

    while b != 0:
        a, b = b, a % b
    return a