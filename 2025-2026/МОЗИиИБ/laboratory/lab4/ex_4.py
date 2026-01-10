def extended_gcd_binary(a: int, b: int):
    """
    Extended binary GCD.
    Returns (g, x, y) such that:
      g = gcd(a, b)
      a*x + b*y = g
    """
    if a == 0:
        return abs(b), 0, 1 if b > 0 else -1 if b < 0 else 0
    if b == 0:
        return abs(a), 1 if a > 0 else -1 if a < 0 else 0, 0

    # Work with positive values for the binary part, but keep originals for identity.
    a0, b0 = a, b
    a, b = abs(a), abs(b)

    # Remove common factors of 2
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    # u = a, v = b
    u, v = a, b
    A, B = 1, 0
    C, D = 0, 1

    while u != 0:
        # while u even
        while (u & 1) == 0:
            u >>= 1
            if (A & 1) == 0 and (B & 1) == 0:
                A >>= 1
                B >>= 1
            else:
                A = (A + b) >> 1
                B = (B - a) >> 1

        # while v even
        while (v & 1) == 0:
            v >>= 1
            if (C & 1) == 0 and (D & 1) == 0:
                C >>= 1
                D >>= 1
            else:
                C = (C + b) >> 1
                D = (D - a) >> 1

        # subtract
        if u >= v:
            u = u - v
            A = A - C
            B = B - D
        else:
            v = v - u
            C = C - A
            D = D - B

    g = v << shift  # restore factors of 2

    # Now we have: a*C + b*D = gcd(a,b) where a,b are abs() reduced ones.
    # Fix signs according to original a0, b0:
    x, y = C, D
    if a0 < 0:
        x = -x
    if b0 < 0:
        y = -y

    return g, x, y
