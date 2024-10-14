def main():

    memo_dict = dict()
    print(f"{fib_func(8, memo_dict)=}")
    print(f"{fib_func(50, memo_dict)=}")
    print(f"{fib_func(1000, memo_dict)=}")


def fib_func(n, memo_dict):
    if n in memo_dict.keys():
        return memo_dict[n]
    # base case
    if n <= 2:
        return 1
    else:
        result = fib_func(n-1, memo_dict) + fib_func(n-2, memo_dict)
        memo_dict[n] = result
        return fib_func(n-1, memo_dict) + fib_func(n-2, memo_dict)


if __name__ == "__main__":
    main()
