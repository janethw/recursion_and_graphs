def sum_func(n):
    if n <= 1:
        return 1
    else:
        return n + sum_func(n-1)


print(f"{sum_func(5)=}")
