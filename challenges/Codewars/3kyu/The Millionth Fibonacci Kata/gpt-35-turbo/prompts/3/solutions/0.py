def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

"""
def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n
"""
