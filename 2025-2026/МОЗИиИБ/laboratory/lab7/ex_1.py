import random
import math

def egcd(a: int, b: int):
    """Extended GCD: returns (g, x, y) with a*x + b*y = g."""
    if b == 0:
        return abs(a), 1 if a > 0 else -1 if a < 0 else 0, 0
    x0, y0, x1, y1 = 1, 0, 0, 1
    aa, bb = a, b
    while bb:
        q = aa // bb
        aa, bb = bb, aa - q * bb
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    g = abs(aa)
    if aa < 0:
        x0, y0 = -x0, -y0
    return g, x0, y0

def modinv(a: int, m: int):
    """Modular inverse of a mod m, if it exists."""
    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    return x % m

def solve_linear_congruence(a: int, b: int, m: int):
    """
    Solve a*x ≡ b (mod m).
    Returns one solution x0 (mod m/g) if solvable, else None.
    """
    g = math.gcd(a, m)
    if b % g != 0:
        return None

    a1 = a // g
    b1 = b // g
    m1 = m // g

    inv = modinv(a1 % m1, m1)
    if inv is None:
        return None
    return (inv * (b1 % m1)) % m1  # solution modulo m1

def pollard_rho_dlp(a: int, b: int, p: int, n: int, max_tries: int = 20, max_steps: int = 200000):
    """
    Solve a^x ≡ b (mod p) using Pollard's Rho for DLP.
    Requires:
      p prime
      n = order of a (so a^n ≡ 1 mod p)
    Returns x in [0, n-1] or None if failed.
    """

    def step(c, u, v):
        # 3-set partition by c % 3
        r = c % 3
        if r == 0:
            # multiply by a
            c = (c * a) % p
            u = (u + 1) % n
        elif r == 1:
            # multiply by b
            c = (c * b) % p
            v = (v + 1) % n
        else:
            # square
            c = (c * c) % p
            u = (2 * u) % n
            v = (2 * v) % n
        return c, u, v

    for _ in range(max_tries):
        # Random start (u, v), then c = a^u * b^v mod p
        u1 = random.randrange(0, n)
        v1 = random.randrange(0, n)
        c1 = (pow(a, u1, p) * pow(b, v1, p)) % p

        u2, v2, c2 = u1, v1, c1  # hare starts same

        for _step in range(max_steps):
            # tortoise 1 step
            c1, u1, v1 = step(c1, u1, v1)
            # hare 2 steps
            c2, u2, v2 = step(c2, u2, v2)
            c2, u2, v2 = step(c2, u2, v2)

            if c1 == c2:
                # (v2 - v1) * x ≡ (u1 - u2) (mod n)
                A = (v2 - v1) % n
                B = (u1 - u2) % n

                x0 = solve_linear_congruence(A, B, n)
                if x0 is None:
                    break  # retry with new random start

                # Verify candidate
                if pow(a, x0, p) == b % p:
                    return x0
                else:
                    break  # retry

    return None


p = 107
a = 10
b = 64
n = 53  # given in the statement

x = pollard_rho_dlp(a, b, p, n)
print("x =", x)
if x is not None:
    print("check:", pow(a, x, p), "==", b % p)
