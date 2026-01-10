import random
import math

def pollards_rho(n: int, c: int = 1, seed: int = 2):
    """
    Pollard's rho factorization.
    Returns a non-trivial factor of n, or None if failed.
    """
    if n % 2 == 0:
        return 2
    if n < 2:
        return None

    def f(x):
        return (x * x + c) % n

    a = seed
    b = seed

    while True:
        a = f(a)
        b = f(f(b))
        d = math.gcd(abs(a - b), n)

        if d == 1:
            continue
        if d == n:
            return None  # failure, retry with different parameters
        return d

n = 1359331
factor = pollards_rho(n, c=5, seed=1)

if factor:
    print("Non-trivial factor found:", factor)
    print("Other factor:", n // factor)
else:
    print("Factor not found, retry with different parameters.")
