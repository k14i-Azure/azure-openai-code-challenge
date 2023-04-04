def fib(n):
    return (lambda x: (x[0], x[1], x[2], x[3]))(lambda x: (x[1], x[0]+x[1], x[2]+1, x[3]+x[0]) if x[2] < n else x)((0, 1, 0, 0))
