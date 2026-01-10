# Euclid’s Algorithm (remainder / division method)
def gcd_euclid(a: int, b: int) -> int:
    """Classic Euclid GCD using remainders."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a

    while b != 0:
        a, b = b, a % b
    return a

gcd = gcd_euclid(45, 10)
print("GCD", gcd)