import math

def f(x:int, n:int):
    return (x**2 + 5) % n 

def pollards_rho(n:int, a:int, b:int):
    while True:   
        a = f(a, n) % n
        b = f(f(b, n), n) % n
        d = math.gcd(a-b, n)
    
        if d > 1 and d < n:
            p = d
            return p
        if d == n:
            print("Factor not found")
            return None
        if d == 1:
            continue
   
print(pollards_rho(1359331, 1, 1))