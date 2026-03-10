

def trim_leading_zeros(arr: list[int])->list[int]:
    """
    Удаляет ведущие нули, но оставляет хотя бы один ноль.
    """
    i = 0
    while i < len(arr) - 1 and arr[i] == 0:
        i += 1
    return arr[i:]

def pad_left(arr: list[int], n: int) -> list[int]:
    """
    Дополняет число слева нулями до длины n.
    """
    if len(arr) == n:
        return arr
    
    i = len(arr) - 1
    new_arr = [0] * n
    j = n - 1
    while i >=0:
        new_arr[j] = arr[i]
        i -= 1
        j -= 1

    while j >= 0 :
        new_arr[j] = 0
        j -= 1
    
    return new_arr 



def add(u:list[int], v:list[int], b:int)-> list[int]:
    """
    Вход:
        u = u1u2...un
        v = v1v2...vn
        b - основание системы счисления

    Выход:
        w = w0w1...wn
    """


    n =  max(len(u), len(v))
    u = pad_left(u, n)
    v = pad_left(v, n)
    w = [0] * (n + 1)

    j = n
    k = 0

    while True:
        u_j = u[j-1]
        v_j = v[j - 1]
        
        w[j] = (u_j + v_j + k) % b
        k =  (u_j + v_j + k) // b
        print(j,w,w[j])

        j = j - 1
        if j > 0:
            continue

        if j == 0:
            w[0] = k
            break
    return trim_leading_zeros(w)

# u = [9,9,8]
# v = [0,7]
# result = add(u, v, 10)
# print("result = ", result)



def Substract(u:list[int], v:list[int], b:int)-> list[int]:
    """
    Вход:
        u = u1u2...un
        v = v1v2...vn
        b - основание системы счисления
        u > v

    Выход:
        w = w0w1...wn = u - v
    """


    n =  max(len(u), len(v))
    u = pad_left(u, n)
    v = pad_left(v, n)
    w = [0] * (n + 1)

    j = n
    k = 0

    while True:
        u_j = u[j-1]
        v_j = v[j - 1]
        
        w[j] = (u_j - v_j + k) % b
        k =  (u_j - v_j + k) // b
        print(j,w,w[j])

        j = j - 1
        if j > 0:
            continue

        if j == 0:
           return trim_leading_zeros(w)

        
    

# u = [9,9,8]
# v = [0,7]
# result = Substract(u, v, 10)
# print("result = ", result)



def multiply(u:list[int], v:list[int], b:int):
    """
    Вход:
        u = u1u2...un
        v = v1v2...vn
        b - основание системы счисления

    Выход:
        w = uv = w1w1...wm+n
    """
    u = trim_leading_zeros(u)
    v = trim_leading_zeros(v)

    n = len(u)
    m = len(v)
    w = [0] *( m + n)

    j = m
    while True:
        if v[j - 1] == 0:
            w[m - j] = 0
        else:
            i = n
            k = 0
            while True: 
                u_i = u[i - 1]
                v_j = v[j - 1]
                w_index = i + j - 1
                t = u_i * v_j + w[w_index] + k
                w[w_index] = t % b
                k = t // b

                i = i - 1
                if i > 0:
                    continue
                else:
                    w[j-1] = k
                    break
        
        j = j - 1
        if j == 0:
            return  trim_leading_zeros(w)
                

# u = [1,2,3]
# v = [4,5]
# b = 10
# result = multiply(u, v, b)
# print("result = ", result)  


def multiply_fast(u:list[int], v:list[int], b:int):
    
    """
    Вход:
        u = u1u2...un
        v = v1v2...vn
        b - основание системы счисления

    Выход:
        w = uv = w1w1...wm+n
    """
    u = trim_leading_zeros(u)
    v = trim_leading_zeros(v)

    n = len(u)
    m = len(v)
    w = [0] *( m + n)
    t = 0
    for s in range(0, m + n):
        for i in range(0, s + 1):
            u_pos = n - i
            v_pos = m - s + i
            if 1 <= u_pos <= n and 1 <= v_pos <= m:
                t = t + u[u_pos - 1] * v[v_pos - 1]
        
        w_index = m + n - s - 1
        w[w_index] = t % b
        t = t // b
    return trim_leading_zeros(w)

# u = [1,2,3]
# v = [4,5]
# b = 10
# result = multiply_fast(u, v, b)
# print("result = ", result)  


def rev_to_int(arr: list[int]) -> int:
        value = 0
        for i in range(len(arr) - 1, -1, -1):
            value = value * b + arr[i]
        return value
    
def int_to_rev(x: int) -> list[int]:
        if x == 0:
            return [0]
        digits = []
        while x > 0:
            digits.append(x % b)
            x //= b
        return digits
    
def get_digit(x_rev: list[int], i: int) -> int:
        return x_rev[i] if 0 <= i < len(x_rev) else 0

def division(u: list[int], v: list[int], b: int) -> tuple[list[int], list[int]]:
    u = trim_leading_zeros(u)
    v = trim_leading_zeros(v)

    if v == [0]:
        return None
    
    u_rev = list(reversed(u))
    v_rev = list(reversed(v))


    n = len(u_rev) - 1
    t = len(v_rev) - 1

    q_rev = [0] * (n - t + 1)

    u_value = rev_to_int(u_rev)
    v_value = rev_to_int(v_rev)

    print("u_value", u_value)
    print("v_value", v_value)

    # Шаг 2:
    # пока u >= v * b^(n-t) выполнять:
    #   q_(n-t) := q_(n-t) + 1
    #   u := u - v * b^(n-t)
    while u_value >= v_value * (b ** (n - t)):
        q_rev[n - t] = q_rev[n - t] + 1 
        u_value = u_value - v_value * (b ** (n - t))
        u_rev = int_to_rev(u_value)

    # Шаг 3: для i = n, n-1, ..., t+1 выполнять пункты 3.1 - 3.4
    for i in range(n, t, -1):
        u_i = get_digit(u_rev, i)
        u_i_minus_1 = get_digit(u_rev, i - 1)
        v_t = get_digit(v_rev, t)
        
        q_index = i - t - 1
        
        if u_i > v_t:
            q_rev[q_index] = b - 1
        else:
            q_rev[q_index] = (u_i * b + u_i_minus_1) // v_t

        # Шаг 3.2
        # пока q_(i-t-1) * (v_t*b + v_(t-1)) > u_i*b^2 + u_(i-1)*b + u_(i-2)
        # выполнять q_(i-t-1) := q_(i-t-1) - 1
        v_t_minus_1 = get_digit(v_rev, t - 1)
        u_i_minus_2 = get_digit(u_rev, i - 2)

        while q_rev[q_index] * (v_t * b + v_t_minus_1) > (u_i * b * b + u_i_minus_1 * b + u_i_minus_2):
            q_rev[q_index] = q_rev[q_index] - 1

        # Шаг 3.3
        # u := u - q_(i-t-1) * b^(i-t-1) * v
        u_value = u_value - q_rev[q_index] * (b ** (i - t - 1)) * v_value
        u_rev = int_to_rev(abs(u_value)) if u_value != 0 else [0]

        # Шаг 3.4
        # если u < 0, то
        #   u := u + v * b^(i-t-1)
        #   q_(i-t-1) := q_(i-t-1) - 1
        if u_value < 0:
            u_value = u_value + v_value * (b ** (i - t - 1))
            q_rev[q_index] = q_rev[q_index] - 1
            u_rev = int_to_rev(u_value)

    # Шаг 4: r := u
    r_rev = int_to_rev(u_value)

    q = trim_leading_zeros(list(reversed(q_rev)))
    r = trim_leading_zeros(list(reversed(r_rev)))

    return q, r



u = [1, 2, 3, 4]
v = [5, 6]
b = 10

q, r = division(u, v, b)
print("q =", q)  # [2, 2]
print("r =", r)  # [0, 2]
