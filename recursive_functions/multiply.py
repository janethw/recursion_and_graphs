def multiply_factorial(n):
    if n <= 0:
        return 1
    else:
        return n * multiply_factorial(n-1)


print(f"{multiply_factorial(5)=}")
