import math

def fermat_factorization(n: int):
    """
    Fermat's factorization.
    Works for odd n.
    Returns (p, q) or None if not found.
    """
    if n <= 0 or n % 2 == 0:
        return None

    s = math.isqrt(n)
    if s * s < n:
        s += 1

    while True:
        t2 = s * s - n
        t = math.isqrt(t2)
        if t * t == t2:
            p = s - t
            q = s + t
            if p != 1 and q != n:
                return p, q
        s += 1



n = 5959  # 59 * 101
factors = fermat_factorization(n)

if factors:
    print("Factors:", factors)
else:
    print("Factors not found.")
