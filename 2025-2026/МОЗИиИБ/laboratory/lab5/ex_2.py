def is_probable_prime_solovay_strassen(n: int, rounds: int = 10) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        g = gcd(a, n)
        if g > 1:
            return False  # composite

        r = pow(a, (n - 1) // 2, n)
        s = jacobi(a, n)  # -1,0,1

        if s == 0:
            return False  # composite (a shares factor with n)

        # Convert s to modulo n: -1 becomes n-1
        s_mod = s % n
        if r != s_mod:
            return False  # composite

    return True  # probably prime
