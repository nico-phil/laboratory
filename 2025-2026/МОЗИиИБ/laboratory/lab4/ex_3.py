#Extended Euclid (returns gcd, x, y)
def extended_gcd_euclid(a: int, b: int):
    """
    Returns (g, x, y) such that:
      g = gcd(a, b)
      a*x + b*y = g
    """
    if b == 0:
        g = abs(a)
        # make x carry the sign of a so identity holds
        x = 1 if a > 0 else -1 if a < 0 else 0
        return g, x, 0

    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y

    g = abs(old_r)
    # Normalize sign so g is positive
    if old_r < 0:
        old_x, old_y = -old_x, -old_y

    return g, old_x, old_y

    
gcd = extended_gcd_euclid(45, 10)
print(gcd)
