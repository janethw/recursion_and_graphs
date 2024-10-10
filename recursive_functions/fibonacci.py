def fib_func(n):
    if n <= 2:
        return 1
    return fib_func(n-1) + fib_func(n-2)


print(fib_func(8))
