from dataclasses import dataclass

@dataclass
class BigInt:
    sign: int        # -1, 0, +1
    digits: list     # least-significant digit first
    base: int

    def normalize(self):
        """Remove leading zeros and fix sign for zero."""
        while len(self.digits) > 0 and self.digits[-1] == 0:
            self.digits.pop()
        if not self.digits:
            self.sign = 0
        return self

def from_int(x: int, base: int) -> BigInt:
    if base < 2:
        raise ValueError("base must be >= 2")
    if x == 0:
        return BigInt(0, [], base)
    sign = 1 if x > 0 else -1
    x = abs(x)
    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base
    return BigInt(sign, digits, base)

def to_int(a: BigInt) -> int:
    """Convert BigInt back to Python int (for testing)."""
    value = 0
    for d in reversed(a.digits):
        value = value * a.base + d
    return a.sign * value

def compare_abs(u: BigInt, v: BigInt) -> int:
    """Compare |u| and |v|: returns -1, 0, +1."""
    if len(u.digits) != len(v.digits):
        return -1 if len(u.digits) < len(v.digits) else 1
    for i in range(len(u.digits) - 1, -1, -1):
        if u.digits[i] != v.digits[i]:
            return -1 if u.digits[i] < v.digits[i] else 1
    return 0




#Algorithm 1: add non-negative numbers (u + v)
def add_nonneg(u_digits, v_digits, base: int):
    """Add two non-negative numbers represented as digit lists (LSB first)."""
    n = max(len(u_digits), len(v_digits))
    w = []
    carry = 0
    for i in range(n):
        ud = u_digits[i] if i < len(u_digits) else 0
        vd = v_digits[i] if i < len(v_digits) else 0
        s = ud + vd + carry
        w.append(s % base)
        carry = s // base
    if carry:
        w.append(carry)
    return w



#Algorithm 2: subtract non-negative numbers (u − v, with u ≥ v)
def sub_nonneg(u_digits, v_digits, base: int):
    """
    Compute u - v for non-negative digits, assuming u >= v (absolute).
    Returns digit list (LSB first).
    """
    w = []
    borrow = 0
    for i in range(len(u_digits)):
        ud = u_digits[i]
        vd = v_digits[i] if i < len(v_digits) else 0
        t = ud - vd - borrow
        if t < 0:
            t += base
            borrow = 1
        else:
            borrow = 0
        w.append(t)

    # trim leading zeros
    while w and w[-1] == 0:
        w.pop()
    return w



#Signed addition/subtraction wrapper
def add_bigint(a: BigInt, b: BigInt) -> BigInt:
    if a.base != b.base:
        raise ValueError("Bases must match")

    # handle zeros
    if a.sign == 0:
        return BigInt(b.sign, b.digits[:], a.base)
    if b.sign == 0:
        return BigInt(a.sign, a.digits[:], a.base)

    # same sign -> add magnitudes
    if a.sign == b.sign:
        digits = add_nonneg(a.digits, b.digits, a.base)
        return BigInt(a.sign, digits, a.base).normalize()

    # different signs -> subtract smaller magnitude from larger magnitude
    cmp = compare_abs(a, b)
    if cmp == 0:
        return BigInt(0, [], a.base)
    if cmp > 0:
        # |a| > |b| => result sign = sign(a)
        digits = sub_nonneg(a.digits, b.digits, a.base)
        return BigInt(a.sign, digits, a.base).normalize()
    else:
        # |b| > |a| => result sign = sign(b)
        digits = sub_nonneg(b.digits, a.digits, a.base)
        return BigInt(b.sign, digits, a.base).normalize()

def sub_bigint(a: BigInt, b: BigInt) -> BigInt:
    # a - b = a + (-b)
    neg_b = BigInt(-b.sign if b.sign != 0 else 0, b.digits[:], b.base)
    return add_bigint(a, neg_b)



#6) Multiplication (schoolbook)
def mul_bigint(a: BigInt, b: BigInt) -> BigInt:
    if a.base != b.base:
        raise ValueError("Bases must match")

    if a.sign == 0 or b.sign == 0:
        return BigInt(0, [], a.base)

    base = a.base
    res = [0] * (len(a.digits) + len(b.digits))

    for i, ad in enumerate(a.digits):
        carry = 0
        for j, bd in enumerate(b.digits):
            res[i + j] += ad * bd + carry
            carry = res[i + j] // base
            res[i + j] %= base
        k = i + len(b.digits)
        while carry:
            res[k] += carry
            carry = res[k] // base
            res[k] %= base
            k += 1

    sign = 1 if a.sign == b.sign else -1
    return BigInt(sign, res, base).normalize()



#Division (quotient and remainder)
def divmod_bigint(u: BigInt, v: BigInt):
    """
    Returns (q, r) where:
      u = q*v + r
      0 <= r < |v|
    """
    if u.base != v.base:
        raise ValueError("Bases must match")
    if v.sign == 0:
        raise ZeroDivisionError("division by zero")

    base = u.base

    # Work with absolute values; fix signs at end
    u_abs = BigInt(1, u.digits[:], base).normalize()
    v_abs = BigInt(1, v.digits[:], base).normalize()

    if u_abs.sign == 0:
        return BigInt(0, [], base), BigInt(0, [], base)

    if compare_abs(u_abs, v_abs) < 0:
        # |u| < |v| => q=0, r=u
        r = BigInt(u.sign, u.digits[:], base).normalize()
        return BigInt(0, [], base), r

    # Helper: multiply a nonneg digit-list by a single digit
    def mul_by_digit(digs, digit):
        carry = 0
        out = []
        for x in digs:
            t = x * digit + carry
            out.append(t % base)
            carry = t // base
        while carry:
            out.append(carry % base)
            carry //= base
        while out and out[-1] == 0:
            out.pop()
        return out

    # Helper: compare two digit-lists (nonneg)
    def cmp_digits(a, b):
        if len(a) != len(b):
            return -1 if len(a) < len(b) else 1
        for i in range(len(a)-1, -1, -1):
            if a[i] != b[i]:
                return -1 if a[i] < b[i] else 1
        return 0

    # Helper: subtract b from a (a>=b), both digit-lists
    def sub_digits(a, b):
        return sub_nonneg(a, b, base)

    # Long division
    q_digits = []
    r_digits = []  # remainder as digit list (LSB first)

    # process from most significant digit to least
    for digit in reversed(u_abs.digits):
        # r = r*base + digit
        r_digits = [digit] + r_digits  # shift left by one base digit
        # normalize r_digits
        while len(r_digits) > 0 and r_digits[-1] == 0:
            r_digits.pop()

        # find quotient digit by binary search in [0, base-1]
        lo, hi = 0, base - 1
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            prod = mul_by_digit(v_abs.digits, mid)
            if cmp_digits(prod, r_digits) <= 0:
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1

        q_digits.append(best)
        # r = r - best*v
        if best != 0:
            prod = mul_by_digit(v_abs.digits, best)
            r_digits = sub_digits(r_digits, prod)

    # q_digits currently MSB->LSB; convert to LSB->MSB
    q_digits = list(reversed(q_digits))
    q = BigInt(1, q_digits, base).normalize()

    # remainder
    r = BigInt(1, r_digits, base).normalize()

    # Fix quotient sign: sign(u)/sign(v)
    q.sign = 0 if q.sign == 0 else (1 if u.sign == v.sign else -1)

    # Fix remainder sign to follow u (common convention)
    r.sign = 0 if r.sign == 0 else u.sign

    return q.normalize(), r.normalize()





if __name__ == "__main__":
    base = 10

    a = from_int(12345678901234567890, base)
    b = from_int(9876543210, base)

    s = add_bigint(a, b)
    d = sub_bigint(a, b)
    m = mul_bigint(a, b)
    q, r = divmod_bigint(a, b)

    print("a =", to_int(a))
    print("b =", to_int(b))
    print("a+b =", to_int(s))
    print("a-b =", to_int(d))
    print("a*b =", to_int(m))
    print("a//b =", to_int(q))
    print("a%b =", to_int(r))

    # verify
    assert to_int(q) * to_int(b) + to_int(r) == to_int(a)
