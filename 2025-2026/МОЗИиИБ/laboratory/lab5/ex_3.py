def is_probable_prime_miller_rabin(n: int, rounds: int = 10) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # write n-1 = 2^s * d with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        witness_found = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                witness_found = False
                break
            if x == 1:
                return False  # composite

        if witness_found:
            return False  # composite

    return True  # probably prime
