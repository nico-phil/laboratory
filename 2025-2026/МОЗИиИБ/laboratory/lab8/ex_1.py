

def trim_leading_zeros(arr: list[int])->list[int]:
    """
    Удаляет ведущие нули, но оставляет хотя бы один ноль.
    """
    i = 0
    while i < len(arr) - 1 and arr[i] == 0:
        i += 1
    return arr[i:]

def pad_left(arr: list[int], n: int) -> list[int]:
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

u = [9,9,8]
v = [0,7]
result = add(u, v, 10)
print("result = ", result)



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

        
    

u = [9,9,8]
v = [0,7]
result = Substract(u, v, 10)
print("result = ", result)




        

        