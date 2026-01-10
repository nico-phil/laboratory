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
