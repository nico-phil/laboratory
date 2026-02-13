import random

def gcd(a: int, b: int) -> int:
    """Greatest common divisor."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def mod_pow(a: int, e: int, n: int) -> int:
    """Fast modular exponentiation: a^e mod n."""
    # Python's built-in pow is already fast and safe.
    return pow(a, e, n)



def is_probable_prime_solovay_strassen(n: int, rounds: int = 10, rng: Optional[random.Random] = None) -> bool:
    """
    Solovay–Strassen:
      pick random a in [2, n-2]
      if gcd(a, n) > 1 -> composite
      r = a^((n-1)/2) mod n
      s = jacobi(a, n)
      compare r with s (mod n)
    """
    if rng is None:
        rng = random.Random()

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(rounds):
        a = rng.randrange(2, n - 1)
        g = gcd(a, n)
        if g > 1:
            return False

        r = mod_pow(a, (n - 1) // 2, n)
        s = jacobi(a, n)
        if s == 0:
            return False

        # s is -1 or 1; compare modulo n
        s_mod = s % n
        if r != s_mod:
            return False

    return True