import time


def countdown(n):
    if n <= 0:
        return 1
    else:
        print(n)
        time.sleep(0.25)
        return countdown(n-1)


countdown(5)
