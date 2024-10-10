def count_up(n):
    if n > 1:
        count_up(n-1)
    print(n)


count_up(6)
