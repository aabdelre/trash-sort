def fun(n):
    if n <= 0: return 0
    if n == 1: return 2
    return fun(n-1) + fun(n-2)
print(fun(6))