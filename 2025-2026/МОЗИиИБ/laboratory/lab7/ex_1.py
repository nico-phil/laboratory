from math import gcd


def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида
    возвращает (g, x, y) такое что

    ax + by = g = gcd(a,b)
    """
    if b == 0:
        return (a, 1, 0)

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return (g, x, y)

def mod_inverse(a, m):
    """
    Обратный элемент a^{-1} mod m
    """
    g, x, _ = extended_gcd(a, m)

    if g != 1:
        return None

    return x % m

def f(value, u, v, p, a, b, r):
    """
    Отображение f из алгоритма.

    Поддерживается инвариант:

        value = a^u * b^v (mod p)
    """

    subset = value % 3

    if subset == 0:

        # value ← value * b
        value = (value * b) % p
        v = (v + 1) % r

    elif subset == 1:

        # value ← value^2
        value = (value * value) % p
        u = (2 * u) % r
        v = (2 * v) % r

    else:

        # value ← value * a
        value = (value * a) % p
        u = (u + 1) % r

    return value, u, v


def pollard_rho_discrete_log(p, a, b, r):
    """
    Реализация алгоритма из конспекта.

    Вход:
        p  — простое число
        a  — элемент порядка r по mod p
        b  — число
        r  — порядок a

    Ищем x:
        a^x ≡ b (mod p)
    """

    # ---------------------------------
    # ШАГ 1
    # выбрать u, v и вычислить
    # c = a^u * b^v (mod p)
    # d = c
    # ---------------------------------

    u_c = 2
    v_c = 2

    c = (pow(a, u_c, p) * pow(b, v_c, p)) % p

    d = c
    u_d = u_c
    v_d = v_c

    step = 0

    print("step | c | log_a(c) | d | log_a(d)")
    print("-----------------------------------")

    while True:

        print(
            step,
            "|",
            c,
            "|",
            f"{u_c}+{v_c}x",
            "|",
            d,
            "|",
            f"{u_d}+{v_d}x",
        )

        # ---------------------------------
        # ШАГ 2
        # c ← f(c)
        # d ← f(f(d))
        # ---------------------------------

        # --- обновление c ---
        c, u_c, v_c = f(c, u_c, v_c, p, a, b, r)

        # --- обновление d два раза ---
        d, u_d, v_d = f(d, u_d, v_d, p, a, b, r)
        d, u_d, v_d = f(d, u_d, v_d, p, a, b, r)

        step += 1

        # ---------------------------------
        # проверяем столкновение
        # ---------------------------------

        if c == d:
            print("\nCollision found")
            break

    # ---------------------------------
    # ШАГ 3
    # приравниваем логарифмы
    #
    # u_c + v_c x = u_d + v_d x (mod r)
    #
    # (v_c - v_d)x = (u_d - u_c) (mod r)
    # ---------------------------------

    A = (v_c - v_d) % r
    B = (u_d - u_c) % r

    print("\nSolve congruence:")
    print(f"{A} * x ≡ {B} (mod {r})")

    g = gcd(A, r)

    if B % g != 0:
        print("No solution")
        return None

    A //= g
    B //= g
    r //= g

    invA = mod_inverse(A, r)

    x = (invA * B) % r

    return x

p = 107
a = 10
b = 64
r = 53

x = pollard_rho_discrete_log(p, a, b, r)

print("\nResult x =", x)

print("Check:")
print(pow(a, x, p))