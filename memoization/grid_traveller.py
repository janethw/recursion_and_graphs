# Routes to travel from top L to bottom R of an m x n grid

def main():
    memo_dict = dict()
    print(f"{grid_traveller(18, 18, memo_dict)}")


def grid_traveller(m, n, memo_dict):
    # check memo_dict
    if (m, n) in memo_dict.keys():
        return memo_dict[(m, n)]

    # base case
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    else:
        left_child = grid_traveller(m-1, n, memo_dict)
        right_child = grid_traveller(m, n-1, memo_dict)
        memo_dict[(m-1, n)] = left_child
        memo_dict[(m, n-1)] = right_child
        return left_child + right_child


if __name__ == "__main__":
    main()