#Binary GCD (Stein’s algorithm)
def gcd_binary(a: int, b: int) -> int:

    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a

    # count common factors of 2
    shift = 0
    while ((a | b) & 1) == 0:  # both even
        a >>= 1
        b >>= 1
        shift += 1

    # make a odd
    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        # make b odd
        while (b & 1) == 0:
            b >>= 1

        # now a and b are odd
        if a > b:
            a, b = b, a
        b = b - a  # b becomes even (difference of odds)

    return a << shift

gcd = gcd_binary(45, 10)
print(gcd)
