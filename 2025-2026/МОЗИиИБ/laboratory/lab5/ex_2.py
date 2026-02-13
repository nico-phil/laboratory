def jacobi(a: int, n: int) -> int:
    """
    Compute Jacobi symbol (a/n) for odd n >= 3.
    Returns: -1, 0, or 1.

    This matches the algorithmic rules typically used in Solovay–Strassen:
      - factor out powers of 2 from a and adjust sign by n mod 8
      - apply quadratic reciprocity when swapping (a, n)
      - reduce a mod n
    """
    if n <= 0 or n % 2 == 0:
        raise ValueError("Jacobi symbol is defined here for positive odd n.")

    a %= n
    result = 1

    while a != 0:
        # Step A: remove factors of 2 from a
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                result = -result

        # Step B: quadratic reciprocity swap
        a, n = n, a  # swap

        if (a % 4 == 3) and (n % 4 == 3):
            result = -result

        a %= n

    # if n == 1 => result, else a became 0 with n>1 => gcd != 1 => 0
    return result if n == 1 else 0


