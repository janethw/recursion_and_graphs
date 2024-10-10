from collections import deque


def main():
    # Simulated inputs
    coins = [50, 100, 200, 1, 2, 5, 10, 20]
    v = 934  # Target value

    # Check if inputs are valid
    if not validate_input(v, coins):
        print("Invalid input. Target value v must be a positive integer."
              " Coins must be a non-empty list of positive integers.")
        return -1

    # Calculate the shortest path to target v given coins[] and having removed duplicates
    min_coins = bfs(v, list(set(coins)))  # returns list of coins required for shortest path

    # Output response to user
    output_result_to_user(v, min_coins)


def bfs(v, coins):
    """ The function uses breadth first search algorithm to calculate the
    minimum number of coins required to achieve a target value v given an
    infinite supply of the coins in the coins list.

    Args:
        - v (int): Represents the target value
        - coins (list): Represents the coin denominations available to reach the target value

    Returns:
        - If target is achievable, returns list: The list of coins used in the shortest path to target value v.
        - If there is no solution, returns int: -1"""

    try:
        queue = deque([(v, [])])
        visited_states_dict = dict()  # list of nodes and paths

        while queue:
            # Take first state from queue
            current_value, current_path = queue.popleft()

            # Determine if this is a new state
            if current_value in visited_states_dict.keys():
                continue
            else:
                visited_states_dict[current_value] = current_path

            # If current_value is zero, target is reached
            if current_value == 0:
                return current_path

            # If target not reached, add neighbouring states (nodes and paths) to queue
            for coin in coins:
                new_value = current_value - coin
                new_path = current_path + [coin]
                queue.append((new_value, new_path))

        return -1

    except (TypeError, MemoryError):
        print("An error occurred")


def validate_input(v, coins):
    """This function validates the input for the target value v and for the coins in the coins list.
    To avoid precision errors, v and elements of coins list must be positive integers.

    Returns:
        - False for invalid inputs
        - True for valid inputs"""
    if not isinstance(v, int) or v <= 0:
        return False
    if not isinstance(coins, list):
        return False
    for coin in coins:
        if not isinstance(coin, int) or coin <= 0:
            return False
    return True


def output_result_to_user(v, min_coins):
    """Function to output the shortest path into a console output to the user"""
    min_coins.sort()
    min_coins_dict = dict.fromkeys(min_coins, 0)

    for coin in min_coins:
        min_coins_dict[coin] += 1
    print(f"Target value {v} can be achieved with a minimum of {len(min_coins)} coins:")
    for coin, count in min_coins_dict.items():
        if count != 0:
            print(f"{count} x coin {coin}")
    return 0


if __name__ == "__main__":
    main()
